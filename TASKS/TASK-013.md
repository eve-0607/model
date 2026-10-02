# TASK-013 — ChatGPT export parser

## Objective
Parse the actual ChatGPT export format into a normalized internal conversation schema.

## READ FIRST
- AGENTS.md
- SPEC/05_PERSONALIZATION.md
- SPEC/11_DATA_GOVERNANCE.md

## Implement
- archive/extraction discovery;
- schema detection from the provided export;
- normalization of conversation IDs, timestamps, roles, message content, and relevant metadata;
- preservation of private source IDs for local traceability;
- malformed-record reporting.

## Acceptance
- complete export parses;
- counts of conversations/messages/tokens or character proxies are reported;
- malformed/unsupported records are logged without aborting the whole corpus;
- raw text is not written to logs by default;
- parser has fixture tests from sanitized examples;
- raw archive remains outside Git.

## Next
TASK-014
