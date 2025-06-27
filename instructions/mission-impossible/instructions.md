# Problem Description

## Background
In the paper *Mission: Impossible Language Models* (Kallini et al. 2024), the authors empirically test whether language models are able to learn possible and impossible languages equally well. They created a set of synthetic 'impossible' languages of varying complexity, demonstrating that GPT-2 (trained from scratch) is unable to learn these languages as well as English (the control). We would like to further investigate this claim by considering artificial languages which 'violate' Greenberg's linguistic universals (generalizations about patterns observed across the world's languages) by introducing structures that are highly unlikely from a linguistic typological perspective.

The paper will be available inside the provided repository in both PDF format as `kallini_et_al_2024.pdf` and markdown format as `kallini_et_al_2024.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the codebase provided (the original codebase of Kallini et al. 2024) to perturb the English data used in the experiments (taken from the BabyLM corpus) and show that GPT-2 trained from scratch is unable to learn languages violating Greenberg universal tendencies as well as a control that does not violate these tendencies. The data should be perturbed applying all of the following three rules:

1. Convert prepositional phrases to postpositional phrases, including embedded prepositional phrases (violating the tendencies of Greenberg's Universal 4).
2. Where there is a definite article (i.e. "the"), and there is an adjective directly preceding the noun, switch the order of the adjective and noun, but only for this adjacent adjective, ignoring comparative and superlative adjectives (deviating from the patterns associated with Greenberg's Universal 18).
3. If there is any determiner followed by a numeral, switch the order of the determiner and numeral (violating the tendencies of Greenberg's Universal 20).

The original BabyLM corpus comprises several data files. Each data file contains multiple dictionaries, each with a batch of annotations (under the "sent_annotations" key), where for each data sample there is a corresponding dictionary with the original text string (under the "sent_text" key) and the constituency parse (under the "constituency_parse" key), also as a string. Please use the constituency parses to perturb the data, and leave code for processing batches of annotations intact.

Constituency parses look like this:
"(ROOT (S (NP (DT The) (CD nine) (JJ red) (JJ fluffy) (NNS cats) (PP (IN of) (PRP$ mine))) (VP (VBZ sleep) (PP (IN on) (NP (DT the) (NN mat))))))"

where the constituent tags are taken from the Penn Treebank tagset.

After applying the rules, the original sentence "The nine red fluffy cats of mine sleep on the mat" should be transformed to "nine The red cats fluffy mine of sleep the mat on".

Please use the `nltk` library in your solution - it is already installed but you may need to import relevant modules in the scripts. Also, please use the `merge_part_tokens()` function in `utils.py` to merge the parse back to a string.

Assume that model checkpoints and the original BabyLM data can be found in the `models/gpt2/` and `babylm_data/` directories respectively, although these may not be visible in the provided repository right now.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate the extension, we will run the following scripts:

- `data/perturb.py` to obtain the train and test data for the synthetic language perturbed according to the rules above
- `training/prepare_training.sh` to generate the config files (using the templates in `training/conf/template/`) for training the model on the synthetic language using `mistral`, a framework for training language models like GPT-2 - `mistral` is installed as a directory in the environment but may not be visible in the provided repository right now 
- `train.py` to launch the training run for the model using the `mistral` framework
- `perplexities/perplexities.py` to obtain test set perplexities for the trained model on a) the test set for the new perturbed language and b) the test set for the control language (i.e. English)

We will run the scripts with `perturbation_type` set to be "shuffle_constituency" - it is important that your solution is named appropriately so it can be referenced correctly. Also, use the same filter method, affect method and GPT-2 tokenizer as for the Shuffle languages in the original paper.

We will use the result files containing test set perplexities saved under `perplexities/` to evaluate the final experimental outcome.