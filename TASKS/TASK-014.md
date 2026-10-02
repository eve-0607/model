# TASK-014 — Personal corpus cleaning and segmentation

## Objective
Turn normalized conversations into reproducible, sanitized training and holdout datasets.

## READ FIRST
- AGENTS.md
- SPEC/05_PERSONALIZATION.md
- SPEC/10_EXPERIMENT_DESIGN.md
- SPEC/11_DATA_GOVERNANCE.md

## Implement
- remove tool traces/noise/empty turns;
- deduplicate exact and near-duplicate examples;
- segment conversations into training units;
- classify stable behavioral data vs mutable state;
- create conversation-level and chronological holdouts;
- emit dataset statistics and hashes.

## Acceptance
- every source record follows a deterministic disposition;
- no conversation overlaps between train and holdout;
- chronological holdout is strictly later than its training cutoff;
- derived datasets are reproducible;
- no raw/private data are committed.

## Next
TASK-015
