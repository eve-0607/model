# TASK-004 — Expert fusion and checkpoint surgery

## Objective
Implement the selected source-to-Eve parameter transformation.

## READ FIRST
- AGENTS.md
- SPEC/02_CHECKPOINTS.md
- RESEARCH/MOESURGERY.md
- DECISIONS.md
- TASKS/TASK-002.md

## Implement
Create a deterministic converter with a manifest describing every tensor:
- copied unchanged;
- reshaped;
- fused;
- cloned;
- averaged/interpolated;
- newly initialized.

For newly initialized tensors, define the initializer and rationale.

## Acceptance
- synthetic mapping tests pass;
- tiny checkpoint conversion passes;
- unchanged tensors match exactly or within an explicit dtype tolerance;
- converted checkpoint reloads;
- conversion manifest is complete;
- source is untouched.

## Stop condition
If a mapping cannot be justified, stop and record the incompatibility instead of inventing one.

## Next
TASK-005
