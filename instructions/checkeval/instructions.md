# Problem Description

## Background
In the paper *CheckEval: A reliable LLM-as-a-Judge framework for evaluating text generation using checklists* (Lee et al. 2024), the authors propose CheckEval, an LLM-as-a-Judge approach designed to improve rating consistency in text generation evaluation. Existing evaluation methods using Likert-scale scoring often suffer from subjectivity, low agreement, and high rating variance across different evaluator models. CheckEval addresses these issues by introducing a checklist-based evaluation framework, where evaluation criteria are decomposed into binary questions, requiring simple yes/no responses. By aggregating these binary judgments across multiple evaluation dimensions, CheckEval produces scores that are more reliable and better correlated with human judgments.

In the setup adopted in the paper, all binary questions are treated with equal weight when being aggregated to produce the final scores. However, some questions may be more important than others for evaluation. Therefore, we want to test if allowing the questions to be weighted leads to improved correlation with human judgments.

The paper will be available inside the provided repository in both PDF format as `lee_et_al_2024.pdf` and markdown format as `lee_et_al_2024.md` if you need to refer to it.

## Extension to be implemented
Your task is to implement a weighting mechanism to aggregate the binary questions in CheckEval, where the weights for each question are obtained by training a linear regression model on 20% of the SummEval dataset. Use the learned weights to determine each binary question's contribution to the final evaluation score on the remainder of the dataset. You should also compute the unweighted score so that we can evaluate whether the weighted score improves upon the correlation with human judgments. After computing both weighted and unweighted scores, compute the correlation with human judgments using Spearman correlation for each score. Note that there are already functions you can use to compute the correlations in the provided repository.

Please use the `scikit-learn` library for linear regression and `google/gemma-2-9b` model's responses to the binary questions. The model responses can be found in `./results_241210/results/gemma-2-9b-it/summeval/multi`. There are four evaluation dimensions (coherence, consistency, fluency, relevance), and you should train a separate linear regression model for each dimension. Make sure to set the random seed to 42 so that the results are replicable.

Please make the experiment runnable by implementing a single script called `run_final.sh` in the root of the repository. This script should call all necessary commands with all parameters specified and should not have any command line arguments itself. It should handle the linear regression model fitting, computing two versions of the CheckEval scores (weighted and unweighted) using the weights from the regression model for the weighted scores, and producing the correlation scores for all four evaluation dimensions for both weighted and unweighted CheckEval scores.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate this extension, we will run the `run_final.sh` script you wrote. The success of the extension will be measured by the average correlation across all evaluation dimensions of unweighted and weighted CheckEval, where:

- Unweighted CheckEval: computes final scores using equal weights for all binary questions
- Weighted CheckEval: computes final scores using weights learned via linear regression on 20% of the SummEval dataset

We will use the dimension-wise correlation scores saved by the script. All results should be saved inside the `./results` directory, using the following naming convention:

- `{dataset}_{model}_correlation.csv` for unweighted CheckEval
- `{dataset}_{model}_weighted_correlation.csv` for weighted CheckEval

Each CSV file should contain correlation results for four evaluation dimensions (coherence, consistency, fluency, relevance). For each dimension, the results should be presented as a row in the CSV along with the corresponding Pearson, Spearman, and Kendall correlation values:

```
dimensions,pearson,spearman,kendall
[dimension],[value],[value],[value]
```

We will use the Spearman correlation values to evaluate the final experimental outcome. 