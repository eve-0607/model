# Evaluation

## Baselines

1. Original Qwen reference.
2. Unmodified student.
3. Student + fixed personalization prompt.
4. Student + conventional SFT.
5. Modified Eve architecture before personalization.
6. Eve + KD.
7. Final Eve.

## Evaluation families

### General capability
Use public, reproducible benchmarks appropriate to the supported modality and report exact benchmark version/config.

### Personalization
Use held-out user interactions. Compare outputs blindly where possible. Human preference from the data owner is one signal; an independent LLM judge is a second signal, not a substitute for human judgment.

### Persistence
Run the same personalization evaluation with the long persona prompt removed. Keep only the minimum operational instruction shared across models.

### Regression
Track language modeling loss/perplexity and selected coding/reasoning benchmarks before and after personalization.

### Inference
Measure prefill/decode latency, tokens/s, peak memory, and speculative acceptance. Record batch/concurrency and hardware.

## Reporting

Do not compress multiple dimensions into one score unless the formula is predefined before evaluation. Report raw metrics and uncertainty/limitations.
