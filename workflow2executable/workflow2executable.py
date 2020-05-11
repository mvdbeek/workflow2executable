import json
import re

import bioblend.galaxy
import requests
from jinja2 import (
    Environment,
    PackageLoader,
)


PARAM_TYPES = {
    'integer': 'int',
    'float': 'float',
    'boolean': 'bool',
    'text': 'str',
    'color': 'str',
}


def get_template():
    env = Environment(
        loader=PackageLoader('workflow2executable.workflow2executable', 'templates'),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template('click_template.py.j2')


def workflow2executable(workflow_id, galaxy_url='https://usegalaxy.org', api_key=None, script_path=None, embedd_workflow=False):
    if api_key:
        gi_args = (galaxy_url, api_key)
    else:
        gi_args = (galaxy_url,)
    gi = bioblend.galaxy.GalaxyInstance(*gi_args)
    workflow = gi.workflows.show_workflow(workflow_id)
    workflow['escaped_name'] = re.sub(r'[^\w_]', '_', workflow['name'].lower())
    inputs = workflow['inputs']
    template_inputs = []
    datasets_to_upload = []
    for step_index, template_input_dict in inputs.items():
        template_input_dict['escaped_variable'] = re.sub(r'[^\w_]', '_', template_input_dict['label'].lower())
        template_input_dict['help'] = workflow['steps'][step_index]['annotation']
        step = workflow['steps'][step_index]
        if step['type'] == 'parameter_input':
            p_type = step['tool_inputs']['parameter_type']
        elif step['type'] == 'data_input':
            p_type = 'click.Path(exists=True)'
            datasets_to_upload.append(template_input_dict['escaped_variable'])
        elif step['type'] == 'data_collection_input':
            p_type = 'click.Path(exists=True)'
        template_input_dict['param_type'] = PARAM_TYPES.get(p_type, p_type)
        template_inputs.append(template_input_dict)
    input_variables = [d['escaped_variable'] for d in template_inputs]
    template_vars = {
        'workflow': workflow,
        'inputs': template_inputs,
        'input_variables': input_variables,
        'datasets_to_upload': datasets_to_upload,
    }
    if embedd_workflow:
        if not api_key:
            # public
            template_vars['full_workflow'] = requests.get("%s/%s" % (gi.base_url, "workflow/export_to_file?id=%s" % workflow_id)).json()
        else:
            template_vars = gi.workflows.export_workflow_dict(workflow_id)
    template = get_template()
    script = template.render(template_vars)
    if script_path is not None:
        with open(script_path, 'w') as out:
            out.write(script)
    else:
        print(script)
