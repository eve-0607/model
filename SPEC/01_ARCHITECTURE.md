# Eve Architecture

Eve is built around three conditionality axes:

1. **Conditional computation** — sparse MoE.
2. **Conditional memory** — n-gram/Engram-style retrieval.
3. **Conditional sequence processing** — hybrid recurrent/delta-style and sparse-attention blocks.

MTP is both a training signal and an inference acceleration mechanism. Eve-Draft is an optional separate speculative decoding subsystem.

## Initial design rule
Keep the source tokenizer and core representation compatible until there is a measured reason to change them.

Do not freeze expert count, expert width, or top-k before TASK-002 audits real tensor shapes and parameter counts.

## Provenance
- Inherited: Qwen reference backbone and compatible infrastructure.
- Adapted: published ideas from conditional memory, MTP, and speculative decoding literature.
- Eve-original: the final active-capacity topology, checkpoint-surgery mapping, distillation/personalization recipe, evaluation protocol, and integrated drafting system.
