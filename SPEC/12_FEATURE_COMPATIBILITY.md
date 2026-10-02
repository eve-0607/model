# Feature Compatibility Matrix

The model contains interacting subsystems. Every feature combination must be tested, not assumed.

| Feature | Dependency | Main risk |
|---|---|---|
| Sparse MoE | EP/communication | routing imbalance, all-to-all cost |
| Hybrid GDN/QSA | kernel/runtime | state/cache correctness |
| Source N-gram | host memory | prefetch latency / bandwidth |
| Engram-style memory | hash/lookup | collision, memory bandwidth |
| MTP | pipeline placement | incompatibilities with some parallelism modes |
| Eve-Draft | verifier/model API | quality loss / poor acceptance |
| White-box KD | shared tokenizer | logit alignment |

The active configuration must record which combinations are enabled.
