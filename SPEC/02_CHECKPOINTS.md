# Checkpoint Policy

Source checkpoints are immutable.

Every generated checkpoint must record source identifier/revision/hash, source config, Eve config, Git SHA, conversion version, tensor mapping, dtype, and validation report.

## Conversion rules

1. Prove mappings on synthetic tensors.
2. Convert a tiny test checkpoint.
3. Validate untouched paths numerically.
4. Validate transformed paths against defined invariants.
5. Convert the production checkpoint only after the above pass.

Never overwrite the source checkpoint and never commit checkpoint bytes.

## Lineage

Every checkpoint must answer: which source weights, code, data, configuration, and conversion produced this artifact?
