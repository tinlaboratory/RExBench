# Problem Description

## Background
The paper *Code Pretraining Improves Entity Tracking Abilities of Language Models* (Kim et al. 2023) has shown that continuing to train language models primarily pretrained on text data on large amounts of code improves the models' entity tracking capacity. This work has further shown that no similar improvement is observed for models additionally trained on math data. We would like to further investigate which kinds of additional training data influences entity tracking. One possible hypothesis is that multimodal models perform better on entity tracking than their text-only counterparts, due to improved grounding.

The aforementioned paper will be available inside the provided repository in both PDF format as `kim_et_al_2023.pdf` and markdown format as `kim_et_al_2023.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the provided codebase to implement an experiment that tests the hypothesis mentioned above about the benefit of multimodal training. Specifically, we would like to see if `Llama-3.2-11B-Vision`, which is a multimodal model trained on top of Llama 3.1 text-only model according to their developers (https://huggingface.co/meta-llama/Llama-3.2-11B-Vision), performs better on entity tracking than its text-only counterpart: `Llama-3.1-8B`.

Assume that all model checkpoints can be found under a directory called `models/` in the repository provided, although this directory may not be visible in the repository right now. The multimodal model's checkpoint will be under `models/Llama-3.2-11B-Vision`, and the text-only model's checkpoint will be under `models/Llama-3.1-8B`. Place the outputs under two different directories `output/Llama-3.1-8B` and `output/Llama-3.2_11B_vision`, each corresponding to each model's outputs. 

The data we will be using to evaluate the model is `data/few_shot_boxes_nso_exp2_max3/test-subsample-states-t5.jsonl`.

Please make the experiment runnable by implementing a single script called `run_final.sh` in the root of the repository. This script should call all necessary commands with all parameters specified and should not have any command line arguments itself. It should handle both experiments as discussed above.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate this extension, we will run the `run_final.sh` script you wrote.

We will use the result files containing the accuracies on 1+ operations saved under the two output directories specified above to evaluate the final experimental outcome.