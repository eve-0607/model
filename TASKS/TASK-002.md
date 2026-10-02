# TASK-002 — Audit source architecture and freeze Eve topology

## Objective
Inspect real checkpoint tensors/configuration. Measure parameter counts, active parameters, layer schedule, expert width/count/top-k, n-gram subsystem, MTP, tokenizer, and checkpoint layout.

Produce 2–3 concrete Eve topology candidates and record the selected one in DECISIONS.md.

## Acceptance
- `docs/source_architecture_audit.md`
- `configs/eve_candidates.yaml` contains verified values
- Tensor dimensions are checked from real files
- A decision record exists before shape-changing surgery

## Next
TASK-003
