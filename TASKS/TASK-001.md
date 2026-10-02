# TASK-001 — Reproduce source checkpoint

## Objective
Load the supplied BF16 Qwen Flash Next checkpoint through the reference path and produce a reproducible fingerprint/loss report.

## Read first
- AGENTS.md
- RESEARCH/QWEN.md
- SPEC/02_CHECKPOINTS.md
- SPEC/08_DISTRIBUTED.md

## Acceptance
- Checkpoint loads.
- Fixed prompts/batch run reproducibly.
- Source weights remain untouched.
- `docs/reference_fingerprint.md` exists.

## Next
TASK-002
