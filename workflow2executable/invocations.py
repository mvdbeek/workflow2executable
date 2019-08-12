import logging
import time

log = logging.Logger(__name__)
TERMINAL_STATES = ('ok', 'error',)


class StepState(object):

    def __init__(self, gi, step_id, order_index, step_label, state):
        self.gi = gi
        self.step_id = step_id
        self.order_index = order_index
        self.label = step_label
        self.state = state
        self.jobs = []
        self.final = False

    def update_from_step_dict(self, step_dict):
        self.step_id = step_dict['id']
        self.state = step_dict['state']
        self.jobs = step_dict['jobs']

    def get_update(self):
        if self.final:
            return
        if self.state == 'error':
            raise Exception('Workflow failed to schedule')
        step_dict = self.gi.workflows.show_invocation_step('null', 'null', self.step_id)
        self.update_from_step_dict(step_dict)
        if self.state == 'scheduled':
            if all(job['state'] in TERMINAL_STATES for job in self.jobs):
                self.final = True

    @property
    def pretty_label(self):
        label = "step {order_index}".format(order_index=self.order_index)
        if self.label:
          label = "{label} - {step_label}".format(label=label, step_label=self.label)
        return label

    def report_progress(self):
        n_ok = 0
        n_error = 0
        n_queued = 0
        n_running = 0
        for job in self.jobs:
            if job['state'] == 'ok':
                n_ok += 1
            if job['state'] == 'error':
                n_error += 1
            if job['state'] == 'running':
                n_running += 1
            if job['state'] == 'queued':
                n_queued += 1
        log.warning("Job states for {pretty_label}:\nOK: {n_ok}, Error: {n_error}, Queued: {n_queued}, Running: {n_running}".format(pretty_label=self.pretty_label, n_ok=n_ok, n_error=n_error, n_queued=n_queued, n_running=n_running))


class InvocationMonitor(object):

    def __init__(self, gi):
        self.gi = gi
        self.step_state_list = []

    def monitor_invocation(self, invocation_id):
        invocation = {'state': 'new'}
        while invocation['state'] == 'new':
            invocation = self.gi.workflows.show_invocation('null', invocation_id)
        for step in invocation['steps']:
            step_state = StepState(
                gi=self.gi,
                step_id=step['id'],
                order_index=step['order_index'],
                step_label=step['workflow_step_label'],
                state=step['state'],
            )
            self.step_state_list.append(step_state)
        while any(s.final is False for s in self.step_state_list):
            for step_state in self.step_state_list:
                step_state.get_update()
                step_state.report_progress()
            time.sleep(1)
        print('Done!')
        # meh, should of course be a nicer summary.
        for step_state in self.step_state_list:
            step_state.report_progress()
