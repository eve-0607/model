# Eve Project Specification

## Objective
Build Eve: a general-purpose, large sparse language model derived from the available BF16 Qwen Flash Next checkpoint, with a substantially larger active compute budget and persistent behavioral personalization.

## Target envelope
Initial design envelope: ~100B–200B total parameters and ~20B–30B active parameters/token. These are targets, not facts; TASK-002 must audit the actual source checkpoint and freeze the concrete topology.

## Core work
- Qwen-derived backbone/reference path
- controlled architecture surgery
- large sparse MoE active budget
- hybrid sequence processing
- conditional n-gram / Engram-style memory experiment
- MTP
- optional Eve-Draft speculative decoding
- white-box teacher distillation
- longitudinal conversational personalization
- rigorous evaluation and ablation

## Non-goals
- Repretraining a frontier model from random initialization.
- Claiming ownership of external model weights or published mechanisms.
- Training directly on the raw private ChatGPT export.
