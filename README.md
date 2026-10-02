# Eve

Eve is an experimental large sparse language-model research project.

The target is a general-purpose model in the ~100B–200B total-parameter class with a substantially larger active compute budget (~20B–30B active/token as an initial design envelope), combining sparse MoE, hybrid sequence processing, conditional n-gram/Engram-style memory, multi-token prediction, and an optional speculative drafting system.

Eve is deliberately **Qwen-derived** rather than a claim of training a frontier foundation model from zero. The intended contribution is the architecture design and surgery, distributed training system, white-box distillation, personalization methodology, evaluation, and inference system.

## Agent workflow

This repository is designed to be driven by a coding agent:

```
do TASK-000
do TASK-001
do TASK-002
...
```

The agent must read `AGENTS.md`, the requested task, and its referenced specifications before making changes.

## Lifecycle

1. Reproduce the supplied BF16 Qwen Flash Next checkpoint.
2. Audit actual tensors and freeze Eve's target topology.
3. Perform controlled architecture surgery.
4. Recover the modified model.
5. Apply white-box teacher distillation.
6. Process the private ChatGPT export into a sanitized behavioral corpus.
7. Personalize Eve and apply preference optimization.
8. Evaluate persistence, capability, and regressions.
9. Add conditional-memory and speculative-drafting experiments.
10. Package reproducible results.

Weights, raw private data, credentials, and large experiment artifacts stay outside Git.

**Start with TASK-000.**
