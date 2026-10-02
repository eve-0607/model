# Qwen Flash Next

Role: primary pretrained substrate and white-box teacher.

TASK-002 must inspect the real checkpoint for:
- exact hidden dimensions
- layer schedule
- attention/GDN structure
- MoE expert count, width, and routing
- n-gram subsystem
- MTP configuration
- tokenizer and special tokens
- checkpoint layout

Do not trust remembered values; verify against the supplied checkpoint and current official implementation.
