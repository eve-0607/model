# TASK-003 — Implement Eve model skeleton

## Objective
Implement the selected Eve architecture in a small/toy form before touching the production checkpoint.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/02_CHECKPOINTS.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- DECISIONS.md

## Implement
- config schema;
- module boundaries;
- source-compatible reference path;
- toy-scale MoE/routing;
- placeholders/interfaces for memory and MTP;
- shape validation.

## Acceptance
- toy model instantiates from YAML;
- forward/backward pass works;
- modules are individually testable;
- no production checkpoint is modified;
- tests cover dimensions and module ordering.

## Next
TASK-004
