# TASK-010 — White-box KD loss

## Objective
Implement the mathematical KD loss used by Eve.

## READ FIRST
- AGENTS.md
- SPEC/04_DISTILLATION.md
- SPEC/03_TRAINING.md
- RESEARCH/DISTILLATION.md

## Implement
Support:
- hard-token CE;
- temperature-scaled teacher/student distributions;
- masked KL loss;
- configurable CE/KD coefficients;
- detached teacher gradients;
- optional compact sparse-logit path.

## Acceptance
- analytical toy example matches a hand-computed result;
- teacher parameters have no gradients;
- student gradients are nonzero on nontrivial input;
- temperature and coefficients are serialized in the run config;
- numerical stability is tested.

## Next
TASK-011
