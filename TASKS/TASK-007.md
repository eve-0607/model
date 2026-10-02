# TASK-007 — Distributed H100 execution

## Objective
Bring Eve to multi-GPU execution. Require a 2-GPU smoke test, expert communication validation, checkpoint save/reload, and a documented 5-GPU dry run.

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
Previous: TASK-006
Next: TASK-008
