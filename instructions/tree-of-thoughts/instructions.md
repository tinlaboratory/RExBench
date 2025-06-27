# Problem Description

## Background
The paper *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (Yao et al. 2023) introduced a new inference framework that builds on top of classic tree-based search algorithms to improve reasoning. The paper reported that on the game of 24 dataset (where four input numbers are used exactly once combined with basic arithmetic operations (`+-*/`) to obtain 24), GPT-4 showed an improved success rate of 74% using the Tree of Thoughts (ToT) algorithm, compared to 4% using standard chain-of-thought prompting. 

The ToT algorithm applied to the game of 24 works as follows: Consider the input "4 9 10 13". For this example, the algorithm would generate different proposals by applying operations between two of the four numbers, reducing the input from four to three numbers. One proposal could be "13 - 9 = 4 (reduced to: 4 4 10)". Next, all the proposals are evaluated, and the top-n promising ones are selected for the next round. For each of the selected proposals, the algorithm generates different proposals to further reduce the three numbers to two. These proposal, evaluation and selection processes are repeated until the model reaches a single number as the final solution (e.g., "13 - 9 = 4 (reduced to: 4 4 10); 10 - 4 = 6 (reduced to: 4 6); 4 * 6 = 24 (reduced to: 24)"). If you want to see actual examples of the game, please refer to the game dataset located at `src/tot/data/24/24.csv`.

To understand further the details of the ToT algorithm and its implementation, you can refer to the original paper in the repository in both PDF format as `yao_et_al_2023.pdf` and markdown format as `yao_et_al_2023.md`.

A pilot follow-up investigation showed that while ToT worked well with GPT-4, for the Deepseek-V2-Lite-Chat model, performance of ToT was worse compared to the standard chain-of-thought baseline. As a starting point to investigating where the exact cause of the worse performance lies, we want to examine how well Deepseek-V2-Lite-Chat carries out one of the steps in the algorithm: selecting promising proposals.

## Extension to be implemented

Your task is to modify the provided repository to investigate how well Deepseek-V2-Lite-Chat performs in a subtask of the ToT method, namely how well it performs in selecting promising proposals compared to GPT-4.

The codebase contains the log file from GPT-4 playing the game of 24. This log file includes the details of GPT-4's performance on each problem. Filter this log file to include only the problems that  are correctly solved by GPT-4 (we will refer to this as the correct subset). To extract the correct subset, you should apply the following logic: a given problem in this dataset is considered "solved" by GPT-4 if any of GPT-4's proposed final solutions uses the four input numbers exactly once, and the proposed final solution evaluates to 24 using the correct arithmetic operations (e.g., "13 - 9 = 4 (reduced to: 4 4 10); 10 - 4 = 6 (reduced to: 4 6); 4 * 6 = 24 (reduced to: 24)"). 

For each problem from the correct subset, identify the 0th step proposals (where the four input numbers are reduced to three) and identify which proposals GPT-4 selects to be used for the next round.

Using these datapoints, evaluate the consistency of Deepseek-V2-Lite-Chat and GPT-4 in selecting proposals. Prompt Deepseek-V2-Lite-Chat to make a selection from GPT-4's 0th step proposals and for each example, compute the precision of Deepseek-V2-Lite-Chat's selection when treating GPT-4's selection as the gold standard. Please report the average precision across all examples in the correct subset.

Assume that model checkpoints can be found in the directory `/stage/hf_cache/DeepSeek-V2-Lite-Chat`, although this may not be visible in the provided repository right now. To accelerate inference speed, we will be using the vLLM framework in a way that passes all the input prompts for this task in one list for automatic batching based on available GPU memory. A vLLM-based chat template is provided in the repository.

Please implement the extension in a new Python file named `eval_deepseek_vllm.py` in the root directory of the repository. Make the experiment runnable by implementing a single script called `run_final.sh` in the root of the repository. This script should call all necessary commands with all parameters specified and should not have any command line arguments itself. In this script, pass the following arguments to the call of `eval_deepseek_vllm.py`:

```

    --task game24 \
    --max_token 512 \
    --seed 6 \
    --task_start_index 900 \
    --task_end_index 1000 \
    --method_generate propose \
    --method_evaluate value \
    --method_select greedy \
    --n_evaluate_sample 3 \
    --n_select_sample 5 

```

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation

To evaluate this extension, we will execute the `run_final.sh` script you wrote. Running the script should produce a `results/precision.json` file that reports the average precision score in the following format:

```
    {
        "average precision": <average precision score>
    }
```

where `<average precision score>` is the average precision score rounded to 3 decimal places. 