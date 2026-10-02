# TASK-000 — Bootstrap repository and environment

## Objective
Make the repository locally installable and establish the development/cluster execution contract.

## READ FIRST
- AGENTS.md
- SPEC/00_PROJECT.md
- SPEC/09_AGENT_EXECUTION.md
- SPEC/08_DISTRIBUTED.md

## Implement
- package the src/eve namespace correctly for editable installation;
- keep runtime dependencies minimal;
- provide scripts/env_report.py;
- provide deterministic import smoke test;
- document the laptop -> mgmt01 -> PBS -> GPU execution path;
- add only lightweight local tooling needed for orchestration and validation;
- update STATUS.md with environment results.

## Acceptance
- python -m pip install -e '.[dev]' succeeds on the laptop;
- python -m pytest -q passes on the laptop;
- python scripts/env_report.py exits 0 on the laptop;
- no checkpoint/private-data files are present in Git;
- repository docs explicitly prevent accidental large-model execution on the laptop.

## Stop condition
Do not install or modify distributed-training stacks in this task.
Do not attempt to access or schedule GPU jobs until TASK-000 local bootstrap is complete.

## Next
TASK-001