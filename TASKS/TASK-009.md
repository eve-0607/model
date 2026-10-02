# TASK-009 — Teacher inference harness

## Objective
Build a resumable Qwen Flash Next teacher runner for generated responses and optional logits.

## READ FIRST
- AGENTS.md
- SPEC/04_DISTILLATION.md
- SPEC/10_EXPERIMENT_DESIGN.md
- RESEARCH/QWEN.md

## Implement
- input manifest with stable prompt IDs;
- resumable batch execution;
- teacher checkpoint hash;
- generation configuration;
- optional logits/top-k capture;
- failure/retry logging.

## Acceptance
- fixed test manifest reproduces outputs/metadata under the same decoding settings;
- interrupted run resumes without duplicating completed examples;
- teacher outputs are stored outside Git;
- artifacts contain lineage metadata.

## Next
TASK-010
