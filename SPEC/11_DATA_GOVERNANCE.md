# Data Governance

The private ChatGPT export is sensitive user data.

Rules:
- raw archive stays outside Git;
- local raw path is provided through configuration/environment, never hard-coded;
- derived datasets get version IDs/hashes without exposing raw records;
- logs must not print full conversation text by default;
- evaluation outputs are sanitized before being published;
- the final public repository may contain only synthetic/redacted examples and aggregate statistics unless explicitly reviewed.

The parser should preserve source IDs privately so a problematic record can be traced and removed without publishing its contents.
