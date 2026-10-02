# Eve

Eve is an experimental large sparse language-model research project.

The project asks whether a pretrained large sparse model can be transformed into a substantially more compute-active architecture, recover its base capability, and then absorb a user's stable interaction policy into the model parameters.

## Current target

Initial design envelope:
- total parameters: ~100B–200B
- active parameters/token: ~20B–30B

These are design targets, not the final architecture. TASK-002 must inspect the actual Qwen checkpoint and perform the accounting before any shape-changing decision is frozen.

## What Eve is

Eve is a Qwen-derived research model. Foundation weights and published mechanisms remain attributed to their authors. The intended Eve work is architecture selection and modification, checkpoint-surgery methodology, large-active-budget sparse routing, distillation and recovery training, longitudinal personalization, evaluation methodology, and optional conditional-memory/speculative-drafting integration.

## Agent workflow

The repository is designed for a coding agent driven one task at a time. The command is simply: do TASK-000, then do TASK-001, and so on.

The agent must obey AGENTS.md, complete acceptance criteria, record evidence, and stop at task boundaries.

## Lifecycle

1. Reference reproduction of the supplied BF16 Qwen Flash Next checkpoint.
2. Source architecture and parameter audit.
3. Freeze a concrete Eve topology.
4. Implement and validate checkpoint surgery.
5. Distributed correctness and recovery training.
6. White-box teacher distillation.
7. Parse/sanitize the private ChatGPT export.
8. Personalize and preference-tune Eve.
9. Evaluate capability retention and weight-level behavioral persistence.
10. Experiment with conditional memory and Eve-Draft.
11. Package reproducible results and provenance.

Raw model weights, private exports, credentials, and large artifacts are never committed.

Start with TASK-000.
