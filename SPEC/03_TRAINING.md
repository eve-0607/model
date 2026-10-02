# Training Plan

## Stage A — Recovery
Continue training the surgically modified model on a licensed/generic capability corpus to recover stable LM behavior.

## Stage B — White-box distillation
Freeze Qwen Flash Next as teacher and train Eve with hard-token CE plus teacher-distribution KD. Prefer online KD or compact sparse-logit representations over full-vocabulary logit caching.

## Stage C — Personalization
Train on sanitized longitudinal conversational data and teacher-refined responses.

## Stage D — Preference optimization
Use corrections/preferences as pairwise supervision.

Base objective:
`L = lambda_ce * CE + lambda_kd * KD + lambda_mtp * MTP`

Weights are experimental configuration, not constants of the project.
