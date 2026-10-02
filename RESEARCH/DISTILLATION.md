# Knowledge Distillation

White-box KD can train Eve against teacher probability distributions in addition to hard labels.

Core requirements:
- teacher is frozen;
- teacher and student tokenization must be compatible for direct vocabulary-level KD;
- temperature, loss coefficient, masking, and reduction are logged;
- online KD is preferred when full-logit caching becomes too large;
- compact sparse/top-k representations are treated as an approximation and evaluated for bias.

References:
- https://arxiv.org/abs/2410.16215
- https://arxiv.org/abs/2505.20888
