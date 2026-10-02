# TASK-009 — Teacher inference harness

## Objective
Build a resumable Qwen Flash Next teacher harness for response generation and optional logits, with prompt IDs, checkpoint hash, generation config, and deterministic metadata.

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
Previous: TASK-008
Next: TASK-010
