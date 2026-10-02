# MTP and Eve-Draft

## MTP

MTP is a future-token prediction objective/module. It can provide additional training signal and can be used by a speculative decoder.

Megatron's current implementation exposes sequential MTP modules and documents placement constraints, including restrictions involving context parallelism. See RESEARCH/MTP.md.

## Eve-Draft

Eve-Draft is a separate speculative decoding subsystem. It proposes candidate tokens/blocks and Eve verifies them.

DSpark is an external serving design; Eve may adapt its semi-autoregressive and confidence-scheduling ideas, but the Eve implementation remains independently measured and attributed.

## Acceptance

No drafting feature is considered successful unless it preserves output correctness while improving a specified latency/throughput metric under a defined serving load.
