# TASK-000 — Bootstrap repository and environment

## Objective
Make the repository locally installable and establish the execution environment contract.

## READ FIRST
- AGENTS.md
- SPEC/00_PROJECT.md
- SPEC/09_AGENT_EXECUTION.md

## Implement
- package the src/eve namespace correctly for editable installation;
- keep runtime dependencies minimal;
- provide scripts/env_report.py;
- provide deterministic import smoke test;
- update STATUS.md with environment results.

## Acceptance
- python -m pip install -e '.[dev]' succeeds;
- python -m pytest -q passes;
- python scripts/env_report.py exits 0;
- no checkpoint/private-data files are present in Git.

## Stop condition
Do not install or modify distributed-training stacks in this task.

## Next
TASK-001
