# TASK-000 — Bootstrap repository and environment

## Objective
Create the initial package, environment report, and deterministic smoke test.

## Read first
- AGENTS.md
- SPEC/00_PROJECT.md
- SPEC/09_AGENT_EXECUTION.md

## Acceptance
- `python -m pytest -q` passes.
- `scripts/env_report.py` exits cleanly.
- No weights or private data are committed.

## Next
TASK-001
