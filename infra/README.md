# Cluster Execution

This directory contains the reproducible cluster-side launch contract for Eve.

## Topology

laptop -> SSH -> mgmt01 (10.16.1.50) -> PBS Professional -> GPU node

The laptop is the development/control plane. mgmt01 is the internet-enabled gateway and PBS submission point. GPU nodes are compute-only and have no internet access.

## Rules

- Never assume a GPU node has internet access.
- Never put credentials in scripts.
- Never hard-code unknown queue/account/resource names.
- Discover cluster-specific PBS syntax on mgmt01 and record it in experiment metadata.
- Stage all network-dependent assets before submitting a GPU job.
- Use versioned scripts rather than copying commands into an interactive shell.
- Start with a smoke test before a long run.
- Capture PBS job ID, resource request, environment versions, Git SHA, config hash, data/checkpoint hashes, and output paths.

## Suggested workflow

1. Develop/test on the laptop.
2. Push/commit the code.
3. SSH to 10.16.1.50.
4. Stage or verify offline dependencies and assets.
5. Submit the versioned PBS job.
6. Inspect PBS status/logs.
7. Collect artifacts/results.
8. Record evidence back in STATUS.md / EXPERIMENTS.md.