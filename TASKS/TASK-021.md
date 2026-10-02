# TASK-021 — Architecture ablations

## Objective
Measure the effect of Eve's active-capacity/topology choices independently of personalization.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/10_EXPERIMENT_DESIGN.md
- RESEARCH/MOESURGERY.md

## Implement
Run matched small-to-medium experiments over the selected candidate family, varying one major architectural factor at a time where possible:
- active expert budget;
- expert topology;
- hybrid layer allocation;
- other frozen design choices.

## Acceptance
- training/evaluation budget is documented;
- parameter counts and measured FLOPs/throughput are reported;
- differences can be attributed to the changed factor with stated limitations.

## Next
TASK-022
