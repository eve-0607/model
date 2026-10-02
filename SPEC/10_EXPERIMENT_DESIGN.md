# Experiment Design

## Principles

A claim is causal only when the competing configurations differ in the claimed component while other important variables are held or explicitly matched.

## Required baseline families

### Architecture
Source Qwen vs modified Eve architecture before personalization.

### Distillation
CE-only vs response-only teacher SFT vs white-box KD.

### Personalization
Unmodified student vs fixed-prompt baseline vs SFT vs SFT+preference optimization.

### Memory
No conditional-memory module vs source Qwen N-gram Embedding vs Eve Engram-style module.

### Drafting
Normal autoregressive generation vs MTP-assisted speculative generation vs Eve-Draft.

## Avoiding leakage

Build evaluation prompts/holdouts before inspecting the final trained outputs. Conversation holdout is by conversation ID, and chronological holdout is created by timestamp. Teacher-generated data must inherit the source split: a teacher must never see evaluation context that becomes a training target.

## Reporting

For every comparison report model revision, dataset hash, number of examples/tokens, hardware, seed, config hash, metric definition, and uncertainty/limitations.
