# TASK-006 — Single-GPU correctness

## Objective
Prove the modified model can forward, backpropagate, save, and reload on one GPU.

## Acceptance
- One training step completes.
- Loss/gradients are finite.
- Reference-preserved modules match within defined tolerance.
- Save/reload preserves outputs.

## Next
TASK-007
