# Problem Description

## Background
In the paper *Explain-then-Translate: An Analysis on Improving Program Translation with Self-generated Explanations* (Tang et al. 2023), the authors investigate the use of self-generated explanations to assist with code-to-code translation using language models. One finding is that natural language explanations help more with difficult problems, but can harm performance on easy problems. The authors demonstrate this by approximating problem hardness as the translation pass@1 score. We would like to further investigate this by building a new difficulty-based problem heuristic to selectively apply explanations to programs, and seeing whether this approach helps improve overall performance.

The paper will be available inside the provided repository in both PDF format as `tang_et_al_2023.pdf` and markdown format as `tang_et_al_2023.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the codebase provided (the original codebase of Tang et al. 2023) to implement a heuristic which computes cyclomatic complexity for a given input function. For functions with a cyclomatic complexity greater than or equal to a specified threshold, add the explanation - otherwise, don't. 

Please use the `radon` library in your solution - it is already installed but you may need to import relevant modules in the scripts.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate the extension, we will run the script `MultiPL-C2C/analysis/post_hoc_selective_explanation.py`. As part of your solution, you should implement a new boolean command-line flag `--cc` in this script to use the cyclomatic complexity heuristic during selection. Leave all other flags the same and do not add any others - we will use the existing `--threshold` flag to set the cyclomatic complexity threshold, using the value of 6.

The script will be applied to data in the `MultiPL-C2C/eval_results` directory, comprising completions for multiple programming language pairs, where Python is always the source language. Each subdirectory contains completions for prompts with and without the explanation.
	
We will use the result file containing pass@1 scores for each programming language pair saved under `translation_results/` to evaluate the final experimental outcome.