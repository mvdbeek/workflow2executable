Turn Galaxy Workflows into standalone scripts.
----------------------------------------------

Totally not ready. Works only with regular dataset inputs
and needs https://github.com/galaxyproject/bioblend/pull/294
to work. Might ultimately fit better into planemo.


The basic idea is that a workflow with completely defined input section
describes itself.

```
python workflow_to_exectable.py 28d1e2d715476c2c https://usegalaxy.org --script_path workflow.py
```

Should create a python script that will run a workflow on a given Galaxy server.
Useage can be seen with `python workflow.py --help`:

```
Usage: workflow.py [OPTIONS]

  Run Select last n lines workflow

Options:
  --input_dataset PATH
  --number_of_lines_to_keep INTEGER
  -a, --api_key TEXT              API key to use for running workflow
  -g, --galaxy_url TEXT           Galaxy URL to use for running workflow
                                  [default: https://usegalaxy.org]
  -h, --history_id TEXT           History ID that will contain workflow
                                  results
  -n, --new_history_name TEXT     Create a new history with this name. Will
                                  not be used if history ID is provided.
  --help                          Show this message and exit.
```
