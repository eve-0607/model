# Eve Architecture

## Design axes

1. Conditional computation: sparse MoE routing.
2. Conditional memory: n-gram/Engram-style lookup.
3. Conditional sequence processing: hybrid GDN/delta-style and sparse-attention blocks.

MTP and speculative drafting are auxiliary training/inference mechanisms, not a reason to redesign every backbone block.

## Initial strategy

Start from the source representation and tokenizer whenever possible. TASK-002 freezes the concrete Eve topology only after inspecting real checkpoint tensors.

## Parameter accounting

Reports must separately publish total model parameters, dense always-active parameters, routed expert parameters active/token, shared expert parameters active/token, conditional-memory table size, memory rows/bytes fetched/token, and MTP/draft-only parameters.

With conditional memory, the phrase active parameters is ambiguous unless these components are reported separately.

## Provenance

Qwen is the inherited substrate. Conditional-memory, MTP, and speculative-drafting ideas are adapted from published work. Eve's final topology, surgery mapping, training recipe, personalization pipeline, and integration are project work to be validated experimentally.
