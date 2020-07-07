===================
workflow2executable
===================


.. image:: https://img.shields.io/pypi/v/workflow2executable.svg
        :target: https://pypi.python.org/pypi/workflow2executable

.. image:: https://img.shields.io/travis/mvdbeek/workflow2executable.svg
        :target: https://travis-ci.org/mvdbeek/workflow2executable

.. image:: https://readthedocs.org/projects/workflow2executable/badge/?version=latest
        :target: https://workflow2executable.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Turn Galaxy Workflows into standalone scripts.


* Free software: MIT license
* Documentation: https://workflow2executable.readthedocs.io.

Turn Galaxy Workflows into standalone scripts.
----------------------------------------------

Works only with regular dataset inputs for now. Might ultimately fit better into planemo.


The basic idea is that a workflow with completely defined input section
describes itself:

.. code-block:: shell

  workflow2executable 28d1e2d715476c2c https://usegalaxy.org --script_path workflow.py


Should create a python script that will run a workflow on a given Galaxy server.
Useage can be seen with 

.. code-block:: shell

 python workflow.py --help

.. code-block:: shell

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
  
    --publish / --private           Publish history?
    --monitor_invocation / --no_monitor_invocation
                                    Print workflow invocation status updates?
    --workflow_id_override TEXT     Override workflow to run with this workflow
                                    id or uuid
  
    --quiet TEXT                    Decrease logging output
    --help                          Show this message and exit.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
