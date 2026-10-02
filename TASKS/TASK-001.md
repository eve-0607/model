# TASK-001 — Reproduce source checkpoint

## Objective
Load the supplied BF16 Qwen3.8-Flash-Next checkpoint through a verified reference path and establish a numerical fingerprint.

## READ FIRST
- AGENTS.md
- RESEARCH/QWEN.md
- SPEC/02_CHECKPOINTS.md
- SPEC/08_DISTRIBUTED.md

## Inputs
The operator supplies the local source-checkpoint path through configuration/environment. Never hard-code a private path.

## Implement
- checkpoint/config inventory;
- tokenizer inventory;
- modality/component inventory;
- deterministic fixed prompts/batches;
- loss/logit/output fingerprint report;
- source hash manifest.

## Acceptance
- checkpoint loads successfully;
- tokenizer round-trip is tested;
- fixed benchmark batch produces reproducible metadata;
- source checkpoint remains byte-for-byte untouched;
- docs/reference_fingerprint.md exists.

## Stop condition
Do not modify the architecture or start training.

## Next
TASK-002
