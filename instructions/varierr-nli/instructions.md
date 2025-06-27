# Problem Description

## Background
In the paper *VARIERR NLI: Separating Annotation Error from Human Label Variation* (Weber-Genzel et al. 2024), the authors explored different methods for automatic error detection in human annotations. We would like to extend this work to consider a new method, adapting the "DM" method in the paper to be trained using model distillation.

The paper will be available inside the provided repository in both PDF format as `weber-genzel_et_al_2024.pdf` and markdown format as `weber-genzel_et_al_2024.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the codebase provided (the original codebase of Weber-Genzel et al. 2024) to train a distilled model on GPT-4o's outputs, using the same prompting method as the "GPT" method in the original paper. The GPT-4o outputs are already obtained for you and can be found in `predictions/gpt-4o/scores.json`, and the original dataset is `varierr.json`.

The trained model should use the same base model as in the original paper, i.e. DistilRoBERTa-base (https://huggingface.co/distilbert/distilroberta-base), and should be a regression model with a sigmoid head, trained using binary cross-entropy loss. For a given annotation, the model input should be:

"{premise} {separator token} {hypothesis} {separator token} {NLI label} {separator token} {reason for annotation}"

where "NLI label" is one of "entailment", "contradiction", "neutral" (in lowercase), and "separator token" is DistilRoBERTa-base's separator token.

Assume that the checkpoints can be found in the `models/distilroberta-base/` directory, although this may not be visible in the provided repository right now.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate the extension, we will run the following scripts:

- `sequence_classification_train.py` to train the classification model on GPT 4o's outputs (3 times with different random seeds)
- `predict_scorers.py` to obtain the regression predictions over the training dataset (3 times for the outputs of each trained model)
- `build_score_table.py` to obtain the final results

As part of your solution, you should add a boolean command-line flag `--distill` (to train with model distillation) and a command-line flag `--distill_fp` (to include the GPT-4o output file path) in both `sequence_classification_train.py` and `predict_scorers.py`. Leave all other flags the same and do not add any others. The model predictions should be aggregated in the same way as the 878 item-label pairs used to train the "DM" models in the paper.

We will use the result file containing precision and recall scores over assigned labels, written out as `results.tsv`, to evaluate the final experimental outcome.