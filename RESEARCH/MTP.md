# Multi-Token Prediction

MTP extends prediction to future tokens and can provide additional training signal and a speculative-decoding path.

Megatron Core's current implementation uses sequential MTP modules with shared embeddings/output heads and documents pipeline placement and compatibility constraints.

References:
- https://github.com/deepseek-ai/DeepSeek-V3
- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/multi_token_prediction.html
