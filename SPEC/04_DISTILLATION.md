# Distillation

Because the complete BF16 Qwen Flash Next teacher is available, Eve can use white-box distillation rather than relying only on generated text.

## Modes

1. Response-only: teacher outputs become hard targets.
2. Online KD: teacher logits are computed during student training and discarded after the loss.
3. Compact offline KD: store only a compact/top-k representation when offline generation is required.
4. Multi-teacher: combine candidate responses or teacher signals from independently verified models; do not average incompatible hidden states.

## Tokenizer constraint

Direct vocabulary-level KD assumes teacher and student use the same tokenization/vocabulary ordering. Eve should retain the source tokenizer unless a later experiment explicitly solves alignment.

## Storage

Do not cache full teacher-vocabulary logits for a massive corpus by default. The storage cost must be estimated before enabling offline logits.

## Loss

The default white-box experiment should compare hard CE against temperature-scaled KL distillation and report temperature, coefficient, masking, and whether the teacher distribution is detached.
