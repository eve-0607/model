# PBS Professional launch scripts

PBS scripts belong here once the cluster audit discovers the real queue, resource, walltime, module, and filesystem conventions.

Do not pre-populate guessed directives.

The eventual scripts should support at least:
- SMOKE=1 for cheap environment/device/distributed checks;
- a task-specific entrypoint;
- explicit working directory;
- explicit stdout/stderr destinations;
- deterministic environment activation;
- no network access assumptions.

A typical lifecycle is:

local test -> SSH to mgmt01 -> stage -> qsub <script.pbs> -> qstat/qstat -f -> collect logs -> record

The first real PBS directives should be filled in by the cluster audit performed during TASK-001.