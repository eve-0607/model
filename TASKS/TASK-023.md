# TASK-023 — Auxiliary teacher and merge experiments

## Objective
Evaluate additional teacher models and compatible distilled checkpoints as optional side experiments.

## READ FIRST
- AGENTS.md
- SPEC/04_DISTILLATION.md
- RESEARCH/MERGING.md
- docs/PROVENANCE.md

## Gate
A checkpoint can enter a weight-space merge experiment only if architecture, tokenizer/vocabulary, initialization lineage, tensor semantics, and licensing/provenance are documented as compatible.

Otherwise use it only for response generation, critique, or evaluation.

## Acceptance
- at least one explicit inclusion/exclusion rationale is recorded;
- no incompatible tensor merge occurs;
- any merged candidate has a complete ancestry manifest.

## Next
TASK-024
