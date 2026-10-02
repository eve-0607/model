# TASK-001 — Reference checkpoint reproduction and cluster audit

## Objective
Load the supplied BF16 Qwen Flash Next checkpoint in a controlled environment, reproduce reference behavior, and inventory the model without changing architecture.

## READ FIRST
- AGENTS.md
- SPEC/01_ARCHITECTURE.md
- SPEC/02_CHECKPOINTS.md
- SPEC/08_DISTRIBUTED.md
- RESEARCH/QWEN.md
- DECISIONS.md

## Execution mode
GPU/PBS.

The full checkpoint is not expected to fit on the development laptop. Prepare and validate the audit code locally, then stage its dependencies/checkpoint on the cluster and execute the audit through PBS.

Normal path:

laptop -> SSH -> mgmt01 -> qsub -> GPU node

GPU compute has no internet access, so the job must run entirely from staged files.

## Implement
- inspect the actual BF16 checkpoint, tokenizer, config, and modality components;
- verify reference loading/inference on the cluster;
- produce a machine-readable architecture/component inventory;
- create a numerical fingerprint for the checkpoint;
- record exact software/environment provenance;
- record cluster/PBS details discovered during execution;
- keep the source checkpoint immutable.

## Required cluster discovery
Before the full audit, discover and record on mgmt01:
- PBS queues and available GPU resources;
- CPU/RAM/walltime limits relevant to the audit;
- usable shared/staging filesystem paths;
- available Python/module/venv environment;
- CUDA/PyTorch/NCCL versions;
- GPU visibility and topology;
- any existing cached model/dependency locations.

Do not guess queue names, resource strings, or module names.

## Acceptance
- reference checkpoint loads successfully;
- reference tokenization/inference smoke test passes;
- architecture/component inventory is produced;
- numerical fingerprint is produced;
- software + hardware + PBS job provenance is recorded;
- no source checkpoint mutation;
- no network access is required by the GPU job.

## Stop condition
Do not make architecture changes. Do not begin TASK-002 automatically.

## Next
TASK-002