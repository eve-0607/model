# Personalization

The ChatGPT export is a longitudinal source for learning stable interaction behavior. It is not copied wholesale into training.

## Derived streams

- normal high-quality conversations;
- explicit user corrections;
- preference statements;
- successful revisions after an error;
- teacher-refined candidate responses;
- negative/undesired examples when their rejection reason is observable.

## What belongs in weights

Stable style and interaction preferences are candidates for weight-level learning.

Fast-changing facts, live project state, credentials, secrets, and mutable environment details should normally remain external memory/context.

## Holdout design

Create both conversation-level and chronological holdouts so nearby turns from the same conversation cannot leak into evaluation.

## Prompt baseline

The prompt-personalized baseline must use a fixed persona/context prompt created without inspecting the evaluation holdout. Its size and contents are logged.
