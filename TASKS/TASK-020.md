# TASK-020 — No-system-prompt persistence

## Objective
Test whether personalization remains measurable when the long persona prompt is removed.

## READ FIRST
- AGENTS.md
- SPEC/05_PERSONALIZATION.md
- SPEC/06_EVALUATION.md
- SPEC/10_EXPERIMENT_DESIGN.md

## Implement
Compare:
1. unmodified student with minimal operational prompt;
2. student with fixed persona prompt;
3. Eve with minimal operational prompt.

Blind the model identity for evaluation where practical.

## Acceptance
- persona prompt was authored before evaluation and did not use holdout content;
- prompt lengths/configurations are recorded;
- held-out metrics and qualitative error categories are reported;
- no single anecdote is treated as proof.

## Next
TASK-021
