# TASK-017 — Personalization SFT

## Objective
Train Eve on the sanitized behavioral corpus while preserving general language-model capability.

## READ FIRST
- AGENTS.md
- SPEC/03_TRAINING.md
- SPEC/05_PERSONALIZATION.md
- SPEC/06_EVALUATION.md

## Experiment
Compare at least:
- Eve architecture before personalization;
- Eve + behavioral SFT;
- a matched non-personalized training control where feasible.

Track general capability and personalization metrics.

## Acceptance
- training checkpoint is loadable;
- held-out personalization results are recorded;
- general-capability regression is measured;
- run lineage is complete.

## Next
TASK-018
