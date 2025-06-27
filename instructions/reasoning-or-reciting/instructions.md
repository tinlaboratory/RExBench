# Problem Description

## Background
The paper *Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks* (Wu et al. 2024), explores whether large language models can generalize to counterfactual tasks. One of the experiments involves a counterfactual version of Python, "ThonPy", which uses 1-based indexing instead of Python's original 0-based indexing. The generalization is measured by comparing LLM performance on HumanEval using Python to ThonPy. Since the original paper only conducts this evaluation on closed-source models, we would like to test how a smaller open-source model would perform on this counterfactual task.

The paper will be available inside the provided repository in both PDF format as `wu_et_al_2024.pdf` and markdown format as `wu_et_al_2024.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the the codebase provided to test the `Llama-3.1-8B-Instruct` model on the code generation task using the HumanEval dataset, using both Python and ThonPy.

Assume that the Llama model can be found in `/stage/cache/Meta-Llama-3.1-8B-Instruct`, although this may not be visible in the provided repository right now.

Make sure to use the following hyperparameters:

- TEMPERATURE=0.1 for pass@1
- TEMPERATURE=0.8 for pass@10
- K=1 for pass@1
- K=10 for pass@10
- NUM_SAMPLES=50

To successfully run inference with the Llama 3 model, please make the following adjustments:

- Use the following template for formatting the inputs:
```
chat_template = (
    "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_message}"
    "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}"
    "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
)
```

- Enable ROPE scaling using the following configuration:
```
model_config.rope_scaling = {
    "type": "dynamic",
    "factor": 8.0,
    "low_freq_factor": 1.0,
    "high_freq_factor": 4.0,
    "original_max_position_embeddings": 8192,
    "rope_type": "llama3"
}
```

Please make the experiment runnable by implementing a single script called `run_final.sh` in the root of the repository. This script should call all necessary commands with all parameters specified and should not have any command line arguments itself. 

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate this extension, we will run the `run_final.sh` script you wrote. The script should generate code predictions and compute the following evaluation metrics:

- pass@1 (temperature=0.1, K=1)
- pass@10 (temperature=0.8, K=10)

We will use the final scores that should be saved in `programming/generation/results/scores.json`. This file should contain results under both standard (0-based) and counterfactual (1-based) indexing conditions.