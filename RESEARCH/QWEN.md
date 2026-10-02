# Qwen3.8-Flash-Next

## Role
Primary pretrained substrate and white-box teacher.

## Verified current reference facts
The official Qwen repository currently describes Qwen3.8-Flash-Next as a multimodal MoE model with a 125B main model, an additional 51B N-gram embedding table, and about 6B activated per token. It uses a Gated DeltaNet + Qwen Sparse Attention hybrid, Gated Residual, N-gram Embedding with host-memory offload, and built-in MTP.

Source: https://github.com/QwenLM/Qwen3.8-Flash-Next
Model card: https://huggingface.co/Qwen/Qwen3.8-Flash-Next

## Audit requirements
TASK-001/002 must inspect the actual supplied checkpoint for exact hidden dimensions, layer schedule, attention/GDN structure, MoE expert count/width/top-k, N-gram subsystem, MTP, tokenizer/special tokens, modality/vision components, and checkpoint layout.

Do not rely on remembered values when exact tensors are available.
