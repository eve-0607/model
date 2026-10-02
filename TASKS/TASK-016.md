# TASK-016 — Teacher-refined personalization data

## Objective
Use Qwen Flash Next to generate candidate/refined responses for selected historical examples. Preserve provenance and protect the evaluation holdout.

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
Previous: TASK-015
Next: TASK-017
