# TASK-018 — Preference optimization

## Objective
Apply pairwise preference optimization using corrections/preferences and teacher candidate comparisons.

## READ FIRST
- AGENTS.md
- SPEC/05_PERSONALIZATION.md
- SPEC/06_EVALUATION.md
- SPEC/03_TRAINING.md

## Implement
Select a documented preference objective (DPO or another justified objective), define reference policy, and version the pair dataset.

## Acceptance
- objective and hyperparameters are logged;
- preference train/holdout split is fixed;
- before/after personalization metrics are compared;
- general-capability regression is checked.

## Next
TASK-019
