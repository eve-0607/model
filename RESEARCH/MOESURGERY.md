# MoE Architecture Surgery

Eve needs a principled route from the pretrained source topology to a larger active expert budget. The main risk is creating a model whose new tensors are random while the old model function is lost.

Relevant literature:
- Sparse Upcycling: https://arxiv.org/abs/2212.05055
- Upcycling Large Language Models into Mixture of Experts: https://arxiv.org/abs/2410.07524
- Net2Net / function-preserving transformations: https://arxiv.org/abs/1511.05641

These works motivate function-preserving or knowledge-reusing transformations. They do not specify Eve's exact surgery. TASK-004 must compare candidate mappings and measure the amount of function preserved before recovery training.
