# Problem Description

## Background
To enhance the reasoning abilities of large language models, the paper *Re-Reading Improves Reasoning in Large Language Models* (Xu et al. 2024) proposed a new prompting strategy of repeating question statements in the input prompts, which showed improved model performance on a variety of math and reasoning benchmarks compared to typical zero-shot chain-of-thought. We would like to test the generalizability of this approach by applying this prompting approach to a new model and dataset.

The paper can be found in the repository in both PDF format as `xu_et_al_2024.pdf` and markdown format as `xu_et_al_2024.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the provided codebase (The Language Model Evaluation Harness from EleutherAI) to test the effectiveness of the re-reading strategy on a new model and a new dataset. Specifically, we want to compare the performance of the `Llama-3.1-8B-Instruct` model with and without the re-reading strategy on the `multistep_arithmetic_two` task of the Big Bench Hard (`bbh`) dataset. For prompting without re-reading, we want to use the zero-shot chain-of-thought prompting template already provided in the codebase (`cot_zeroshot`). For prompting with re-reading, we want to keep this setting but repeat the question once in the prompt with the string "\nRead the question again:" in between the repeated questions.

Assume that the Llama model can be found in `/stage/cache/Meta-Llama-3.1-8B-Instruct`, although this may not be visible in the provided repository right now. Use a batch size of 4 for running inference. In addition, `Llama-3.1-8B-Instruct` requires model-specific prompt tokens to achieve expected performance. You may need to find a way in the repository's documentation to use a model-specific template to format your input.

Please make the experiment runnable by implementing the following two scripts: 1. `lm-evaluation-harness/rereading-results/bbh_cot_zeroshot_multistep_arithmetic_two_llama.sh`, which is a shell script for running the evaluation without re-reading, and 2. `lm-evaluation-harness/rereading-results/bbh_cot_zeroshot_multistep_arithmetic_two_reread_llama.sh`, which is a shell script for running the evaluation with re-reading. These scripts should include all necessary commands with all parameters specified and should not have any command line arguments themselves.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate the extension, we will run the `bbh_cot_zeroshot_multistep_arithmetic_two_llama.sh` and `bbh_cot_zeroshot_multistep_arithmetic_two_reread_llama.sh` scripts that you wrote.

Please make sure that the results are written to the following directories:

Results of Experiment 1 (using `bbh_cot_zeroshot_multistep_arithmetic_two_llama.sh`): `lm-evaluation-harness/rereading-results/bbh_cot_zeroshot_multistep_arithmetic_two_llama`

Results of Experiment 2 (using `bbh_cot_zeroshot_multistep_arithmetic_two_reread_llama.sh`): `lm-evaluation-harness/rereading-results/bbh_cot_zeroshot_multistep_arithmetic_two_reread_llama`

We will use the results files in these two directories to evaluate the final experimental outcome. 