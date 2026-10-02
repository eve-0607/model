# Eve Project Specification

## Objective

Develop Eve as a general-purpose sparse model derived from the supplied BF16 Qwen Flash Next checkpoint, with a larger active compute budget, modern hybrid sequence processing, optional conditional memory, MTP/speculative inference, and weight-level personalization from longitudinal interaction data.

## Scope

1. Reference reproduction.
2. Architecture audit and surgery.
3. Capability recovery/distillation.
4. Personalization.
5. Evaluation.
6. Optional memory and drafting experiments.

## Target envelope

Initial target: ~100B–200B total parameters and ~20B–30B active parameters/token.

The source checkpoint may contain non-text components. TASK-001 must inventory modalities/components. Eve v1 is text-generation-first unless TASK-002 establishes a justified multimodal preservation path.

## Success evidence

The final report must show source/reference reproduction, exact Eve parameter accounting, checkpoint lineage, recovery/distillation methodology, held-out personalization evaluation, capability-regression evaluation, no-system-prompt persistence, and major ablations.

## Non-goals

- Frontier-scale pretraining from random initialization.
- Passing external model mechanisms off as Eve-original.
- Treating the raw private export as an unrestricted training corpus.
