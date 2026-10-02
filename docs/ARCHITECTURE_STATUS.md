# Architecture Status

**Not frozen before TASK-002.**

Current design envelope:
- total parameters: ~100B–200B
- active parameters/token: ~20B–30B

These are target ranges only.

TASK-002 must calculate the actual source model structure and propose concrete expert count, expert width, routing top-k, layer schedule, conditional-memory budget, and MTP configuration.

Do not launch full-scale training before the topology decision is recorded in DECISIONS.md.
