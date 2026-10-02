# Eve Agent Contract

You are the implementation agent for Eve. Execute the requested task, not a different task you think is better.

## Workflow
1. Read `AGENTS.md`.
2. Read the requested `TASKS/TASK-XXX.md`.
3. Read every file listed under READ FIRST.
4. Inspect current code and repository state.
5. Plan briefly.
6. Implement only the task scope.
7. Run every required test.
8. Record commands/results in STATUS.md or EXPERIMENTS.md.
9. Stop.

## Hard rules
- Never fabricate benchmark results.
- Never claim a test passed unless it was run.
- Never silently change the architecture.
- Architectural ambiguity: record it in DECISIONS.md and stop.
- Never overwrite source checkpoints.
- Never commit model weights, raw ChatGPT exports, credentials, or private data.
- Every checkpoint surgery operation needs a documented tensor mapping.
- Distributed code gets a single-device correctness test first.
- Do not launch expensive H100 jobs unless the task explicitly calls for them.
- Preserve a reference implementation for optimized paths.

## Provenance
Explicitly distinguish inherited, adapted, and Eve-original work. Do not claim external published mechanisms as original Eve inventions.
