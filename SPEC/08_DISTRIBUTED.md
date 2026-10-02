# Distributed Execution

Initial target hardware: 5x NVIDIA H100 80 GB.

Candidate parallelism:
- tensor parallelism
- expert parallelism
- pipeline parallelism
- context parallelism

Every distributed task must have:
- single-device correctness
- multi-GPU smoke test
- reproducible launch configuration
- checkpoint save/reload verification
