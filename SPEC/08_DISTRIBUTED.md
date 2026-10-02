# Distributed Execution

## Cluster topology

Initial experimental hardware: 5x NVIDIA H100 80 GB.

Development and execution are split across three layers:

1. Laptop / development plane
   - HP OmniBook X Flip 14
   - Intel Core Ultra 7 285V
   - 32 GB RAM
   - source editing, code review, lightweight tests, config/manifests, and orchestration only;
   - do not plan around fitting the full model or training locally.

2. mgmt01 / gateway plane
   - address: 10.16.1.50;
   - internet-enabled;
   - SSH entry point to the university compute environment;
   - used to stage dependencies/data/model assets when internet access is required;
   - used to submit PBS Professional jobs;
   - not assumed to be a GPU execution host.

3. GPU / compute plane
   - H100 nodes;
   - no internet access;
   - reachable only through mgmt01;
   - work launched by PBS Professional;
   - jobs must be self-contained with all required files/dependencies already staged.

Execution path:

laptop -> SSH -> mgmt01 -> qsub -> GPU node

## PBS execution contract

All GPU tasks must have a reproducible job script under a repository-controlled PBS directory (or a task-specific equivalent).

A job script must declare:
- resource requirements;
- walltime;
- queue/project/account only after discovery;
- working directory;
- environment activation;
- exact task entrypoint;
- output/log paths;
- smoke-test vs full-run mode.

Cluster-specific values must be discovered on mgmt01 rather than guessed. Examples include qstat output, available queues, resource names, GPU resource syntax, CPU/RAM limits, walltime limits, and module/venv layout.

## Offline compute rule

A GPU job must be reproducible with network access disabled.

Before submission, verify that all required packages, compiled libraries, model weights, tokenizers, datasets, configuration files, and auxiliary assets are already available through the cluster filesystem or staged job input.

Never make a GPU job depend on pip install, git clone, wget, curl, Hugging Face downloads, telemetry endpoints, or similar network access.

## Dependency and asset staging

Internet-dependent acquisition belongs on mgmt01 or another approved internet-enabled host.

Use a staged-artifact manifest that records at minimum:
- artifact name;
- source URL/repository;
- version or commit;
- local/staged path;
- checksum;
- acquisition timestamp;
- license/provenance where relevant.

The GPU job should consume the staged artifact by checksum/path and must not re-fetch it.

## Parallelism

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
- 5-GPU dry-run;
- logged CUDA, PyTorch, NCCL, Transformer Engine/Megatron versions;
- logged PBS job ID and resource request;
- captured parallelism config;
- verified offline/no-network behavior for compute jobs.

## Failure handling

A cluster execution failure must identify which layer failed:
- laptop orchestration;
- SSH/gateway access;
- PBS submission/queueing;
- environment staging;
- GPU job startup;
- distributed initialization;
- training/runtime;
- checkpoint/output staging.

Do not hide infrastructure failures as model failures.