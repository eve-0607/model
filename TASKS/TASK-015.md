# TASK-015 — Corrections and preferences

## Objective
Extract naturally occurring supervision about what the user accepts, rejects, or asks to change.

## READ FIRST
- AGENTS.md
- SPEC/05_PERSONALIZATION.md
- SPEC/06_EVALUATION.md

## Implement
Detect and preserve:
- explicit corrections;
- explicit style/preferences;
- dissatisfaction/rejection when unambiguous;
- successful revisions after a correction.

Each example must retain private provenance internally and a public-safe identifier.

## Acceptance
- extraction is reproducible;
- ambiguous signals are flagged rather than treated as labels;
- train/holdout separation is preserved;
- a manually inspectable sanitized sample is produced locally.

## Next
TASK-016
