# TASK-007 — Distributed H100 execution

## Objective
Move the validated Eve model to distributed execution on the available H100 cluster.

## READ FIRST
- AGENTS.md
- SPEC/08_DISTRIBUTED.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- DECISIONS.md

## Execution mode
GPU/PBS.

Development and orchestration happen on the laptop; execution occurs on GPU nodes through mgmt01 and PBS Professional.

## Implement
Select and document TP/EP/PP/CP only after measuring model layout and communication. Use Megatron Core or another justified distributed substrate.

Create reproducible PBS launch scripts with:
- discovered queue/resource syntax;
- explicit working directory;
- environment activation;
- smoke/full-run mode;
- stdout/stderr paths;
- exact entrypoint;
- required artifact paths.

Before any multi-GPU run, verify the same code path on one GPU.

## Acceptance
- 2-GPU forward/backward smoke test;
- expert communication validated;
- distributed checkpoint save/reload;
- 5-GPU dry-run;
- launch config and environment captured;
- PBS job IDs and resource requests recorded;
- GPU job succeeds without internet access.

## Stop condition
No long training run.

## Next
TASK-008