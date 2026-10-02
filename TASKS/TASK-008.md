# TASK-008 — Architecture recovery training

## Objective
Recover the modified model's language-model function before personalizing it.

## READ FIRST
- AGENTS.md
- SPEC/03_TRAINING.md
- SPEC/06_EVALUATION.md
- SPEC/10_EXPERIMENT_DESIGN.md
- RESEARCH/MOESURGERY.md

## Experiment
Run short controlled comparisons:
1. modified architecture + CE;
2. modified architecture + source-teacher KD;
3. source/reference control.

Use a licensed/generic corpus and fixed validation data.

## Acceptance
- all runs use matched evaluation protocol;
- validation loss/perplexity and training throughput are recorded;
- routing statistics are recorded;
- at least one recovery checkpoint is loadable;
- experiment lineage is complete.

## Stop condition
Do not proceed to massive-scale training unless the recovery experiment passes its defined gates.

## Next
TASK-009
