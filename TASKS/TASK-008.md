# TASK-008 — Architecture recovery training

## Objective
Run controlled recovery training on licensed/generic data. Compare validation behavior against the source/reference model before proceeding to expensive runs.

## Read first
- `AGENTS.md`
- relevant `SPEC/` files
- relevant `RESEARCH/` notes

## Scope
Implement only this task. Preserve source checkpoints and private data.

## Acceptance criteria
- Required implementation/tests exist.
- Results are actually executed and recorded.
- No fabricated metrics.
- Any architecture ambiguity is recorded in `DECISIONS.md` and the task stops.
- Large/long H100 jobs are launched only when explicitly required by this task.

## Dependencies
Previous: TASK-007
Next: TASK-009
