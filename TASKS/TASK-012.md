# TASK-012 — Multi-token prediction

## Objective
Implement MTP as a separable subsystem and verify training/inference behavior.

## READ FIRST
- AGENTS.md
- SPEC/07_MTP_DRAFT.md
- SPEC/08_DISTRIBUTED.md
- RESEARCH/MTP.md

## Implement
- future-token target construction;
- MTP module(s);
- MTP loss;
- configurable loss weighting;
- optional speculative verification interface.

## Acceptance
- future-token indices are analytically verified;
- MTP loss is numerically tested;
- save/reload works;
- disabling MTP restores the non-MTP path;
- distributed placement follows the documented compatibility constraints.

## Next
TASK-013
