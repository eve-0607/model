# Agent Execution

Every task is a transaction:

READ -> PLAN -> IMPLEMENT -> TEST -> RECORD -> STOP

## Task authority

The task file defines the implementation scope and acceptance gate. Specs define architectural intent. Source papers/repos define external reference behavior.

## Execution classification

Before doing work, classify each command as:
- LOCAL — safe/lightweight on the 32 GB laptop;
- GATEWAY — intended for mgmt01, usually internet/staging/PBS control work;
- GPU/PBS — requires scheduled compute on a GPU node.

The agent should keep the laptop responsive and should not accidentally launch a large training or model-load operation locally.

## When a task needs the cluster

Use the sequence:
1. make the code/config change locally;
2. run the cheapest local tests available;
3. commit/preserve the code state;
4. SSH to mgmt01 at 10.16.1.50;
5. stage/check required offline dependencies and assets;
6. submit a PBS job;
7. wait/poll using PBS tooling;
8. collect stdout/stderr, job metadata, metrics, and checkpoints;
9. return to the laptop and record the result in the repository.

Do not treat a successful qsub submission as task completion. Completion requires the requested job outcome and evidence.

## PBS jobs

Every non-trivial GPU execution must be reproducible from a versioned job script.

The script should support a cheap smoke mode so that environment, imports, device visibility, distributed initialization, and filesystem access can be validated before an expensive run.

Cluster-specific queue/resource syntax must be discovered on mgmt01. Do not guess it in repository code.

## Offline compute

GPU nodes have no internet access. Therefore:
- no runtime downloads;
- no dependency installation from public indexes;
- no source-code fetches;
- no remote logging endpoints that require internet;
- no hidden fallback to external model/data downloads.

Resolve and stage network-required assets before PBS execution.

## Artifacts and lineage

For every remote run, capture:
- Git SHA;
- task ID;
- checkpoint identifier/hash;
- dataset identifier/hash;
- config hash;
- seed;
- cluster host/gateway;
- PBS job ID;
- queue/resource request;
- software/module versions;
- start/end timestamps;
- output and checkpoint paths;
- exit status.

## When blocked

If the agent discovers an architectural incompatibility, missing source information, cluster capability issue, or a choice that changes a frozen decision:
1. record the evidence in DECISIONS.md;
2. do not silently choose a substitute;
3. stop at the task boundary.

## Evidence

A task is complete only when its acceptance criteria are backed by executed commands or produced artifacts. A clean code diff alone is not evidence of correctness.