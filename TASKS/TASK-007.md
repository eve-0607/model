# TASK-007 — Distributed H100 execution

## Objective
Move the validated Eve model to distributed execution on the available H100 cluster.

## READ FIRST
- AGENTS.md
- SPEC/08_DISTRIBUTED.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- DECISIONS.md

## Implement
Select and document TP/EP/PP/CP only after measuring model layout and communication. Use Megatron Core or another justified distributed substrate.

## Acceptance
- 2-GPU forward/backward smoke test;
- expert communication validated;
- distributed checkpoint save/reload;
- 5-GPU dry-run;
- launch config and environment captured.

## Stop condition
No long training run.

## Next
TASK-008
