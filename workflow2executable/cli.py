# -*- coding: utf-8 -*-

"""Console script for workflow2executable."""
import sys
import click

from workflow2executable.workflow2executable import workflow2executable


@click.command('workflow2executable')
@click.argument('workflow_id')
@click.argument('galaxy_url')
@click.option('-a', '--api_key', help="Provide API key if workflow is private.")
@click.option('-s', '--script_path', help="Write generated script to this path. If not provided prints script to stdout.")
@click.option('--embedd_workflow/--no_embedd_workflow', default=False, help="Include workflow in generarted script?")
def main(workflow_id, galaxy_url, api_key, script_path, embedd_workflow):
    workflow2executable(workflow_id, galaxy_url, api_key, script_path, embedd_workflow)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
