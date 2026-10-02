# TASK-006 — Single-GPU correctness

## Objective
Prove the full modified Eve model can run one forward/backward/save/reload cycle on one GPU.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/02_CHECKPOINTS.md
- DECISIONS.md

## Acceptance
- one training step completes;
- loss and gradients are finite;
- save/reload preserves outputs within tolerance;
- source-preserved portions match reference behavior;
- memory usage is recorded;
- a smoke checkpoint is saved outside Git.

## Stop condition
Do not start multi-GPU work until this task passes.

## Next
TASK-007
