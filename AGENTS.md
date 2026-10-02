# Eve Agent Contract

You are the implementation agent for Eve. Execute the requested task, not a different task you think is better.

## Required workflow

1. Read AGENTS.md.
2. Read the requested TASKS/TASK-XXX.md.
3. Read every exact path listed under READ FIRST.
4. Inspect the current repository and relevant source checkpoint/code.
5. Determine whether the work is LOCAL, GATEWAY, or GPU/PBS before execution.
6. Write a short execution plan before implementation.
7. Implement only the task scope.
8. Run every required test and validation command.
9. Record commands, metrics, artifacts, and failures.
10. Update STATUS.md and/or EXPERIMENTS.md.
11. Stop. Do not silently begin the next task.

## Execution topology

The development machine is a laptop with limited local compute:
- HP OmniBook X Flip 14
- Intel Core Ultra 7 285V
- 32 GB RAM

Treat the laptop as the development/control plane, not the model-training machine. Local work should include repository editing, static analysis, small deterministic tests, config generation, manifests, dataset parsing/validation that fits in memory, and other lightweight tasks.

The university cluster is a separate compute plane:
- gateway/management node: 10.16.1.50 (mgmt01);
- mgmt01 has internet access;
- GPU compute nodes have no internet access;
- GPU nodes are reachable only through mgmt01;
- GPU work is scheduled through PBS Professional.

The normal execution path is:

laptop -> SSH -> mgmt01 -> PBS submission -> GPU node

Do not assume direct laptop-to-GPU SSH, internet access from GPU jobs, Docker pulls from compute nodes, or arbitrary package installation on GPU nodes.

Any task requiring H100 access must provide or use:
- a reproducible PBS job script;
- explicit resource requests;
- an explicit working directory;
- environment/module/venv activation;
- explicit stdout/stderr paths;
- a non-interactive command suitable for qsub;
- a smoke-test mode before a long run.

Do not invent cluster-specific queue names, account strings, node properties, module names, filesystem paths, or GPU resource syntax. Discover them on mgmt01 and record the discovered values before relying on them.

Because mgmt01 is the internet-enabled gateway, dependency/model/data acquisition that requires internet access should happen there or on another approved internet-enabled host, then be transferred/staged for offline GPU execution. Compute jobs must not silently attempt to download packages, model files, datasets, or telemetry.

Prefer source-controlled code/configuration over ad-hoc commands typed on cluster nodes. Cluster-side state that matters for reproducibility must be recorded in manifests or experiment metadata.

## Hard rules

- Never fabricate a result, benchmark number, or successful test.
- Never silently alter a frozen architecture decision.
- If a required decision is missing, record the blocker in DECISIONS.md and stop.
- Never overwrite or mutate source model weights.
- Never commit model weights, private conversation exports, credentials, or large generated artifacts.
- Every checkpoint transformation needs a deterministic mapping manifest.
- Every numerical optimization path needs a reference implementation or toy equivalence test.
- Distributed code requires single-device correctness before multi-GPU execution.
- Expensive H100 jobs need an explicit task-level reason and a completed smoke test.
- Preserve experiment lineage: Git SHA, checkpoint hash, dataset version/hash, config hash, hardware, seed, PBS job ID, queue/resource request, environment/module versions, and output paths.
- Keep external mechanism provenance visible in code/docs.

## Claims discipline

Distinguish inherited, adapted, and Eve-original work. Do not describe external mechanisms as original Eve inventions.

## Private-data discipline

Raw ChatGPT exports remain outside Git. Derived datasets must be reproducible from a local source export but must not expose the raw source by default.

## Architecture-change gate

Changes to tokenizer, hidden size, layer count/order, attention family, routing topology, expert count/width/top-k, conditional-memory design, MTP, or drafting architecture require a recorded decision before implementation proceeds.