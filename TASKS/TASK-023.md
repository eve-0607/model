# TASK-023 — Auxiliary teacher and merge experiments

## Objective
Evaluate additional teachers or compatible weight-space merges only when lineage, architecture, tokenizer, and licensing are verified.

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
Previous: TASK-022
Next: TASK-024
