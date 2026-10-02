# Eve Master Plan

## Phase 0 — Establish the reference
TASK-000 → TASK-002
- bootstrap;
- reproduce the source BF16 checkpoint;
- audit real tensors and freeze Eve topology.

**Gate:** no shape-changing implementation before TASK-002 records a concrete decision.

## Phase 1 — Architecture surgery
TASK-003 → TASK-007
- toy/model skeleton;
- checkpoint surgery;
- routing;
- single-GPU correctness;
- distributed H100 execution.

**Gate:** converted model must pass deterministic correctness checks before recovery training.

## Phase 2 — Recover the source function
TASK-008
Use generic/licensed data and source-teacher supervision to recover capability lost through architecture surgery.

**Gate:** show controlled CE/KD recovery results before large runs.

## Phase 3 — Teacher distillation and MTP
TASK-009 → TASK-012
- teacher harness;
- white-box KD;
- distillation experiments;
- MTP.

## Phase 4 — Personalization
TASK-013 → TASK-018
- parse export;
- clean/segment/split;
- extract corrections/preferences;
- teacher-refine;
- SFT;
- preference optimization.

**Gate:** evaluation holdout is immutable before personalization training starts.

## Phase 5 — Evidence
TASK-019 → TASK-021
- build unified evaluator;
- no-system-prompt persistence experiment;
- architecture ablations.

## Phase 6 — Conditional memory and inference research
TASK-022 → TASK-024
- Engram-style memory;
- auxiliary teachers/compatible merges;
- Eve-Draft speculative decoding.

These are optional branches after the main Eve model is stable; failure here does not invalidate the core model.

## Phase 7 — Release
TASK-025
Produce the reproducible research/demo package.

## Task dependency rule

Tasks are intentionally sequential for the coding agent. Parallel research may happen outside the repository, but the agent should not skip a task's acceptance gate.
