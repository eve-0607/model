# Engram / Conditional Memory

DeepSeek's Engram work treats conditional memory as a sparsity axis complementary to MoE. The mechanism uses hashed n-gram lookup with context-aware fusion, giving near-constant lookup cost with respect to memory-bank size.

Paper: https://arxiv.org/abs/2601.07372
Code: https://github.com/deepseek-ai/Engram

For Eve, distinguish the source Qwen N-gram Embedding from an Engram-style redesign. The source mechanism should not be replaced merely because Engram exists; TASK-022 measures whether a separate design helps.
