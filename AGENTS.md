# Eve Agent Contract

You are the implementation agent for Eve. Execute the requested task, not a different task you think is better.

## Required workflow

1. Read AGENTS.md.
2. Read the requested TASKS/TASK-XXX.md.
3. Read every exact path listed under READ FIRST.
4. Inspect the current repository and relevant source checkpoint/code.
5. Write a short execution plan before implementation.
6. Implement only the task scope.
7. Run every required test and validation command.
8. Record commands, metrics, artifacts, and failures.
9. Update STATUS.md and/or EXPERIMENTS.md.
10. Stop. Do not silently begin the next task.

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
- Preserve experiment lineage: Git SHA, checkpoint hash, dataset version/hash, config hash, hardware, seed, and output paths.
- Keep external mechanism provenance visible in code/docs.

## Claims discipline

Distinguish inherited, adapted, and Eve-original work. Do not describe external mechanisms as original Eve inventions.

## Private-data discipline

Raw ChatGPT exports remain outside Git. Derived datasets must be reproducible from a local source export but must not expose the raw source by default.

## Architecture-change gate

Changes to tokenizer, hidden size, layer count/order, attention family, routing topology, expert count/width/top-k, conditional-memory design, MTP, or drafting architecture require a recorded decision before implementation proceeds.
