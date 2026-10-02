# TASK-005 — Router and expert routing

## Objective
Implement Eve's sparse router for the selected topology and verify routing behavior.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/12_FEATURE_COMPATIBILITY.md
- DECISIONS.md

## Implement
- routing logits;
- top-k selection;
- routing normalization;
- capacity/overflow policy if used;
- load statistics;
- deterministic test mode;
- distributed-ready routing interfaces.

## Acceptance
- fixed input gives reproducible routing;
- expert counts match configured topology;
- routing probabilities are valid;
- selected experts receive gradients;
- load statistics are emitted;
- toy backward pass remains finite.

## Next
TASK-006
