# Problem Description

## Background
In the paper *Instruction Following without Instruction Tuning* (Hewitt et al. 2024), the authors find that language models can still exhibit instruction-following behaviour without being explicitly instruction-tuned. One method they show achieves this is modifying the language model's distribution using handwritten rules. The rule-based experiments are run with Llama-2-7B, using 3 rules:

1. Upweighting the score of the EOS token linearly with response length (in favor of shorter responses). The length-dependent score is calculated as: (length of response)*15/250
2. Uniformly modifying the probabilities of 15 particular tokens in the vocabulary at every token decision.
3. Penalizing the generation of repeated tokens by adding a penalty weight of -1.5 to any tokens generated so far.

The new language model distribution is then calculated as a product of the pretrained language model distribution and the rule-based distribution.

While the other two experiments in the paper experimented with the OLMo-7B language model in addition to Llama-2-7B, this was not done for the rule-based experiment. We would like to see to what extent the rule-based experiment from Llama generalizes to OLMo.

The paper will be available inside the provided repository in both PDF format as `hewitt_et_al_2024.pdf` and markdown format as `hewitt_et_al_2024.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the codebase provided (the original codebase of Hewitt et al. 2024) to extend the rule-based implementation to OLMo-7B-July2024 ([https://huggingface.co/allenai/OLMo-7B-0724-hf](https://huggingface.co/allenai/OLMo-7B-0724-hf)). You should use the same three rules outlined above, and change them as necessary to be compatible with OLMo-7B-July2024.

Assume that model checkpoints can be found in a directory `models/OLMo-7B-0724-hf`, although this may not be visible in the provided repository right now.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate the extension, we will run three scripts, located in `scripts/iclr2025/expt3_olmo/`. For each script, we will use the OLMo-7B-July2024 model by passing the model path `models/OLMo-7B-0724-hf` as the environment variable `$MODEL_PATH`. Each script generates responses from a model using the rule-based implementation with a different ablation by calling the script `eval/alpaca_farm/run_eval.py`. Then, each script runs AlpacaEval for the generated responses from the rule-based model against responses from 5 finetuned OLMo-7B-July2024 models (using different seeds), located in `results/alpaca_farm/`. The scripts to be run are:

- `rule_based_eval_all.sh` (uses all 3 rules)
- `rule_based_eval_eos-uniform.sh` (uses rules 1 and 2)
- `rule_based_eval_none.sh` (uses no rules, i.e. just the pretrained language model distribution)

We will use the result files containing length controlled win-rates from the AlpacaEval evaluation saved under `results/alpaca_farm/` to evaluate the final experimental outcome.

You should *not* modify these scripts at all.