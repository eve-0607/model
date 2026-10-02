# TASK-022 — Conditional-memory experiment

## Objective
Evaluate a dedicated n-gram/Engram-style conditional-memory subsystem separately from the source Qwen N-gram Embedding path.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- RESEARCH/ENGRAM.md
- RESEARCH/MEMORY_GRAFTING.md

## Implement
- hash/addressing path;
- lookup table;
- context-aware fusion/gating;
- configurable memory size;
- optional host-memory/offload path.

## Acceptance
- hash/lookup collisions and shapes are tested;
- no-memory, source-memory, and Eve-memory conditions are distinguishable;
- memory bandwidth/latency is measured;
- capability effect is evaluated under matched conditions.

## Next
TASK-023
