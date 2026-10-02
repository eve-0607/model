# Distributed Execution

Initial experimental hardware: 5x NVIDIA H100 80 GB.

The exact parallelism plan is discovered from the audited model and actual cluster topology rather than assumed from GPU count.

Potential dimensions:
- tensor parallelism;
- expert parallelism;
- pipeline parallelism;
- context parallelism where supported.

## Compatibility gate

Do not assume all dimensions compose. For example, current Megatron MTP documentation lists context parallelism as unsupported with its MTP implementation. Such constraints must be reflected in the active run configuration.

## Required validation

- one-GPU correctness;
- two-GPU distributed smoke test;
- checkpoint save/reload across ranks;
- production-scale dry run before long training;
- logged CUDA, PyTorch, NCCL, Transformer Engine/Megatron versions and parallelism config.
