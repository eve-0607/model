# Architecture Status

**Not frozen before TASK-002.**

Current design envelope:
- total parameters: ~100B–200B
- active neural parameters/token: ~20B–30B

The source Qwen3.8-Flash-Next reference currently reports a 125B main model plus a 51B N-gram embedding table and approximately 6B activated per token. Those source figures are context for the audit, not Eve's final values.

The final architecture must separately report:
- dense always-active parameters;
- routed expert parameters active/token;
- shared-expert parameters active/token;
- conditional-memory table size;
- memory rows/bytes retrieved/token;
- MTP/draft-only parameters.

Do not collapse these into one number without a definition.
