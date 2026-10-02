# TASK-016 — Teacher-refined personalization data

## Objective
Use Qwen Flash Next as a teacher to improve selected historical interaction targets without copying teacher mistakes blindly.

## READ FIRST
- AGENTS.md
- SPEC/04_DISTILLATION.md
- SPEC/05_PERSONALIZATION.md
- SPEC/10_EXPERIMENT_DESIGN.md

## Implement
For selected training examples:
- generate multiple teacher candidates where practical;
- retain the historical response as a reference;
- preserve candidate provenance and decoding settings;
- optionally score/critique candidates;
- never send holdout examples into the teacher-generation training pipeline.

## Acceptance
- candidate dataset has stable IDs and lineage;
- generated targets are distinguishable from historical source text;
- evaluation holdout is excluded;
- storage volume is estimated before any logits are cached.

## Next
TASK-017
