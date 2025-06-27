# Problem Description

## Background
The paper *WinoDict: Probing language models for in-context word acquisition* (Eisenschlos et al. 2023) attempts to measure LLMs' ability to learn novel words during inference. They rewrite Winograd-style co-reference resolution problems by replacing the key concept word with a synthetic but plausible English word and adding the definition of the new concept as a suffix. Building on this work, we would like to further consider a learning setting where the form of the learned words coincides with existing English words and explore how their existing meanings may interfere with the models' word acquisition from the given definition. The hypothesis is that overriding existing words would be more difficult, and the frequency of the existing words may also modulate the effect.

The paper will be available inside the provided repository in both PDF format as `eisenschlos_et_al_2023.pdf` and markdown format as `eisenschlos_et_al_2023.md` if you need to refer to it.

## Extension to be implemented
Your task is to modify the codebase provided to generate new Winodict datasets by replacing the target word being learned with an existing English word. The new dataset should be stored under the directory `./data`. Your replacement should consider the POS tags of the original word - they should be matched. We will only consider four POS categories for word replacement: nouns, verbs, adjectives, and adverbs. To test the possible effect of frequency, sample the candidates from different frequency groups:

1. Top Group:
    - Verbs, Nouns, Adverbs: Select the top 20% most frequent words
    - Adjectives: Select the top 35% most frequent adjectives (to match the sample set size)
2. Bottom Group:
    - Verbs, Nouns, Adverbs: Select the bottom 20% least frequent words
    - Adjectives: Select the bottom 35% least frequent adjectives.
3. All Group:
    - Verbs, Nouns, Adjectives, Adverbs: Include all words, no frequency-based filtering
    
Assume that the frequency information will be provided in a form of four files corresponding to each POS, named `1_all_rank_noun.txt`, `2_all_rank_verb.txt`, `3_all_rank_adjective.txt`, `4_all_rank_adverb.txt`, under the directory `./words/`. Each file lists words in descending order of frequency from the British National Corpus. To generate the dataset, you need to create word candidates based on the files and sample words from those candidates.

From each group, sample words from the candidate lists to generate the new Winodict dataset. Ensure that the replacement word is inflected to match the morphological properties of the original word being replaced. For instance, if the original word is a past tense verb, the selected replacement must also be in the past tense. Please use `spaCy` with the `lemminflect` module to inflect the selected words as necessary.

Using the new dataset, you should run experiments on the Winodict-Winograd dataset under the 5-shot setting. Assume that the model can be found under `/stage/hf_cache/gemma-2-9b`, although this may not be visible in the provided repository right now. Furthermore, we will only consider the setting where definitions are appended as suffixes, which are represented as the `last_def` template in the codebase. Save your results as three different files under `./results/`, corresponding to the three sampling groups defined above. They should be named `res_top.json`, `res_bottom.json`, and `res_all.json`.

Please make the experiment runnable by implementing a single script called `run_final.sh` in the root of the repository. This script should call all necessary commands with all parameters specified and should not have any command line arguments itself. It should handle both the dataset generation as well as the execution of the experiments on this new dataset.

Try your best to keep everything else not specified above constant in the original repository. Also, the environment is already set up, so you do not need to install any dependencies or download any more datasets/models. Please refer to `environment.yml` in the repository for an overview of the installed libraries and their versions.

### Evaluation
To evaluate the extension, we will execute the `run_final.sh` script you wrote. We will use the three `.json` files mentioned above that contain the final results to evaluate the experimental outcome.