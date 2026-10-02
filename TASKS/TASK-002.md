# TASK-002 — Audit source architecture and freeze Eve topology

## Objective
Measure the real source checkpoint and convert the project target into concrete architecture candidates.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/02_CHECKPOINTS.md
- SPEC/10_EXPERIMENT_DESIGN.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- RESEARCH/QWEN.md
- RESEARCH/MOESURGERY.md

## Audit
Measure exact:
- total parameter count;
- dense always-active parameters;
- routed expert count, width, and source top-k;
- layer schedule;
- hidden dimensions and attention dimensions;
- GDN/QSA components;
- residual structure;
- source N-gram table;
- MTP components;
- tokenizer/vocabulary;
- modality/vision components;
- checkpoint tensor naming/layout.

## Design
Produce 2–3 concrete Eve candidates in configs/eve_candidates.yaml. Each candidate must have exact parameter accounting and an explicit mapping strategy from the source.

## Decision gate
Record exactly one selected candidate (or record that no candidate is yet viable) in DECISIONS.md.

## Acceptance
- docs/source_architecture_audit.md;
- verified config with tensor-derived values;
- parameter accounting script/output;
- explicit candidate mapping;
- decision record before any shape-changing implementation.

## Next
TASK-003
