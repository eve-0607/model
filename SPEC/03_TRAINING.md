# Training Plan

## Stage 0 — Reference
Reproduce the source model and verify tokenization, loss, checkpoint loading, and inference before modifying parameters.

## Stage 1 — Architecture surgery
Create the modified Eve checkpoint using only verified tensor mappings. Do not train on personal data here.

## Stage 2 — Recovery / bridge training
Use a licensed/generic corpus plus the source model as a teacher. The goal is to recover the modified model's language-model function before personalization. Compare CE-only, teacher-KD, and mixed objectives on short controlled runs.

## Stage 3 — White-box distillation
Freeze Qwen Flash Next. Train Eve with hard CE plus teacher-distribution KD. When teacher and student tokenizers match, align logits directly; otherwise use a documented sequence-alignment method.

## Stage 4 — Personalization
Train only on sanitized derived datasets from the private export. Keep general capability data mixed in to reduce catastrophic specialization.

## Stage 5 — Preference optimization
Use correction/preference pairs after supervised personalization. Record the reference model and objective used for preference optimization.

## Objective

Base form:

L_total = lambda_ce * L_CE + lambda_kd * L_KD + lambda_mtp * L_MTP + lambda_pref * L_pref

Terms may be disabled by stage. All nonzero weights are experiment configuration, not fixed project constants.
