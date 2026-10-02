# Distillation

Because the full BF16 Qwen Flash Next teacher is available, Eve can use white-box distillation.

Use three controlled modes:
1. response-only distillation;
2. online logit KD;
3. compact sparse-logit/offline KD.

Do not save full-vocabulary logits for a giant corpus by default.

Other models can supply candidate answers or teacher signals. Tensor merging is a separate experiment and is allowed only for compatible lineages and architectures.
