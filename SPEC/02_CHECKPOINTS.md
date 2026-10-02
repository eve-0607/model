# Checkpoint Policy

Source checkpoints are immutable.

Every conversion must emit:
- source config snapshot
- source checkpoint hash
- output config
- tensor mapping
- conversion version
- logs

Shape-changing operations require deterministic synthetic-tensor tests before touching real model weights.

Never store checkpoints in Git.
