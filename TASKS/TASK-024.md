# TASK-024 — Eve-Draft speculative decoding

## Objective
Implement and evaluate a separate speculative draft/verification path.

## READ FIRST
- AGENTS.md
- SPEC/07_MTP_DRAFT.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- RESEARCH/DSPARK.md

## Implement
- candidate drafting;
- target-model verification;
- acceptance metrics;
- batch/concurrency-aware scheduling interface if justified.

## Acceptance
- output correctness is preserved;
- tokens/sec and latency are measured;
- acceptance length/rate is recorded;
- memory use is recorded;
- comparison uses identical prompts and serving conditions.

## Next
TASK-025
