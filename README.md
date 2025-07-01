<div align="center">

<!-- # RExBench : Can coding agents autonomously implement AI research extensions? -->
<img src="assets/rex.png" alt="RExBench Title" width="800">

**Nicholas Edwards**¹*, **Yukyung Lee**²*, **Yujun (Audrey) Mao**², **Yulu Qin**², **Sebastian Schuster**¹³†, **Najoung Kim**²†

¹University College London, ²Boston University, ³University of Vienna

*, † Equal contribution

[Paper](https://arxiv.org/abs/2506.22598) | [Website](https://rexbench.com/) | [Dataset 🤗](https://huggingface.co/datasets/tin-lab/RExBench)

</div>

### 📊 Submission Page
Submit your agent here : [Go submission page 🚀](https://rexbench.com/submission)

### 📂 Repository Structure

```bash
.
├── instructions/            # Task-specific instructions (see list below)
│   ├── checkeval/
│   ├── cogs/
│   ├── entity-tracking-multimodal/
│   ├── explain-then-translate/
│   ├── implicit-ins/
│   ├── mission-impossible/
│   ├── othello/
│   ├── reasoning-or-reciting/
│   ├── re-reading/
│   ├── tree-of-thoughts/
│   ├── varierr-nli/
│   └── winodict/
└── process_instructions.py     # Script for processing instructions
```

Each subdirectory inside instructions/ contains an instructions.md file that describes the task setting.

### ✅ Included Tasks
* checkeval
* cogs
* entity-tracking-multimodal
* implicit-ins
* mission-impossible
* othello
* reasoning-or-reciting
* re-reading
* tree-of-thoughts
* varierr-nli
* winodict

### 🧠 Baseline Agents
* Agent 1: aider ([GitHub](https://github.com/tinlaboratory/aider))
* Agent 2: OpenHands ([GitHub](https://github.com/tinlaboratory/OpenHands))
* Agent 3: Claude Code

### Citation

```bibtex
@article{edwards2025rex,
        title={RExBench: Can coding agents autonomously implement AI research extensions?},
        author={Edwards, Nicholas and Lee, Yukyung and Mao, Yujun (Audrey) and Qin, Yulu and Schuster, Sebastian and Kim, Najoung},
        journal={arXiv preprint},
        year={2025}
        }
```

### Contact
Team RExBench (rexbench@googlegroups.com)