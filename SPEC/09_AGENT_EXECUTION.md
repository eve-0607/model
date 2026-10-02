# Agent Execution

Every task is a transaction:

READ -> PLAN -> IMPLEMENT -> TEST -> RECORD -> STOP

## Task authority

The task file defines the implementation scope and acceptance gate. Specs define architectural intent. Source papers/repos define external reference behavior.

## When blocked

If the agent discovers an architectural incompatibility, missing source information, or a choice that changes a frozen decision:
1. record the evidence in DECISIONS.md;
2. do not silently choose a substitute;
3. stop at the task boundary.

## Evidence

A task is complete only when its acceptance criteria are backed by executed commands or produced artifacts. A clean code diff alone is not evidence of correctness.
