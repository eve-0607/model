# TASK-019 — Evaluation harness

## Objective
Build a reproducible evaluation system covering capability, personalization, persistence, regression, and inference.

## READ FIRST
- AGENTS.md
- SPEC/06_EVALUATION.md
- SPEC/10_EXPERIMENT_DESIGN.md

## Implement
- fixed benchmark manifest;
- model adapters;
- deterministic decoding mode where appropriate;
- metric registry;
- JSON/CSV/Markdown result outputs;
- blind personal-preference evaluation interface;
- latency/throughput measurement.

## Acceptance
- every baseline runs through the same harness;
- benchmark/version/config hashes are recorded;
- results can be regenerated from manifests;
- no evaluation prompt comes from a training split.

## Next
TASK-020
