# Hydra Ray AWS Example

## Getting Started
1) Install Poetry

2) Install dependencies
```bash 
poetry install
```

3) Run app on AWS Ray cluster
```bash
python my_app.py --multirun task=1,2,3
```

## Errors

### First Error
```
[2024-07-21 10:43:47,244][HYDRA] Ray Launcher is launching 3 jobs, 
[2024-07-21 10:43:47,244][HYDRA]        #0 : task=1
[2024-07-21 10:43:47,319][HYDRA]        #1 : task=2
[2024-07-21 10:43:47,391][HYDRA]        #2 : task=3
[2024-07-21 10:43:47,469][HYDRA] Pickle for jobs: /tmp/tmp6574t01r/job_spec.pkl
Cluster: default

2024-07-21 10:43:47,480 INFO util.py:382 -- setting max workers for head node type to 0
Checking AWS environment settings
Traceback (most recent call last):
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/utils.py", line 220, in run_and_report
    return func()
           ^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/utils.py", line 466, in <lambda>
    lambda: hydra.multirun(
            ^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/hydra.py", line 162, in multirun
    ret = sweeper.sweep(arguments=task_overrides)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/core_plugins/basic_sweeper.py", line 177, in sweep
    results = self.launcher.launch(batch, initial_job_idx=initial_job_idx)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra_plugins/hydra_ray_launcher/ray_aws_launcher.py", line 62, in launch
    return _core_aws.launch(
           ^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra_plugins/hydra_ray_launcher/_core_aws.py", line 106, in launch
    return launch_jobs(
           ^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra_plugins/hydra_ray_launcher/_core_aws.py", line 117, in launch_jobs
    sdk.create_or_update_cluster(
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/sdk/sdk.py", line 38, in create_or_update_cluster
    return commands.create_or_update_cluster(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/commands.py", line 314, in create_or_update_cluster
    config = _bootstrap_config(config, no_config_cache=no_config_cache)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/commands.py", line 408, in _bootstrap_config
    validate_config(config)
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/util.py", line 162, in validate_config
    raise e from None
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/util.py", line 160, in validate_config
    jsonschema.validate(config, schema)
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/jsonschema/validators.py", line 1332, in validate
    raise error
jsonschema.exceptions.ValidationError: Additional properties are not allowed ('autoscaling_mode', 'initial_workers', 'target_utilization_fraction' were unexpected)

```

### Second Error

(After commenting out the additional entries)
```
Traceback (most recent call last):
  File "/tmp/tmp.tTUvsfPQn6/_remote_invoke.py", line 18, in <module>
    from ._launcher_util import (
ImportError: attempted relative import with no known parent package
Shared connection to 3.79.57.96 closed.
Traceback (most recent call last):
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/utils.py", line 220, in run_and_report
    return func()
           ^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/utils.py", line 466, in <lambda>
    lambda: hydra.multirun(
            ^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/hydra.py", line 162, in multirun
    ret = sweeper.sweep(arguments=task_overrides)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra/_internal/core_plugins/basic_sweeper.py", line 177, in sweep
    results = self.launcher.launch(batch, initial_job_idx=initial_job_idx)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra_plugins/hydra_ray_launcher/ray_aws_launcher.py", line 62, in launch
    return _core_aws.launch(
           ^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra_plugins/hydra_ray_launcher/_core_aws.py", line 106, in launch
    return launch_jobs(
           ^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib/python3.12/site-packages/hydra_plugins/hydra_ray_launcher/_core_aws.py", line 154, in launch_jobs
    sdk.run_on_cluster(
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/sdk/sdk.py", line 109, in run_on_cluster
    return commands.exec_cluster(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/commands.py", line 1167, in exec_cluster
    result = _exec(
             ^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/commands.py", line 1233, in _exec
    return updater.cmd_runner.run(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/command_runner.py", line 383, in run
    return self._run_helper(final_cmd, with_output, exit_on_fail, silent=silent)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/philipp/Repositories/hydra-aws-example/.venv/lib64/python3.12/site-packages/ray/autoscaler/_private/command_runner.py", line 291, in _run_helper
    raise click.ClickException(
click.exceptions.ClickException: Command failed:

  ssh -tt -i /home/philipp/.ssh/hydra-philipp.pem -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o IdentitiesOnly=yes -o ExitOnForwardFailure=yes -o ServerAliveInterval=5 -o ServerAliveCountMax=3 -o ControlMaster=auto -o ControlPath=/tmp/ray_ssh_7aa2b466ee/7505d64a54/%C -o ControlPersist=10s -o ConnectTimeout=120s ec2-user@3.79.57.96 bash --login -c -i 'source ~/.bashrc; export OMP_NUM_THREADS=1 PYTHONWARNINGS=ignore && (python /tmp/tmp.tTUvsfPQn6/_remote_invoke.py /tmp/tmp.tTUvsfPQn6)'

```
