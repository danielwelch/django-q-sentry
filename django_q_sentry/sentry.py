import sys
import traceback

import sentry_sdk
from sentry_sdk.integrations.logging import ignore_logger

# Important to not log the logger.error nessages from django-q
# We only want to catch the exceptions, not the logger
ignore_logger('django-q')


def return_task_from_stack(tb) -> dict:
    """
    Function returns task information from stack trace if available
    Used to tag
    :param tb: traceback
    :return return_task: dict
    """
    return_task = {}
    if not tb:
        tb = sys.exc_info()[2]
    while 1:
        if not tb.tb_next:
            break
        tb = tb.tb_next
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    traceback.print_exc()
    for frame in stack:
        for key, value in frame.f_locals.items():
            if 'task' == key and isinstance(value, dict):
                if value.get('id', False) and value.get('func'):
                    return value
    return return_task



class Sentry(object):

    def __init__(self, dsn, **kwargs):
        sentry_sdk.init(dsn, **kwargs)

    def report(self):
        error = sys.exc_info()
        tb = error[2]
        task = return_task_from_stack(tb)
        with sentry_sdk.push_scope() as scope:
            scope.set_extra('django_q_task_id', task.get('id', ''))
            scope.set_extra('django_q_task_name', task.get('name', ''))
            scope.set_extra('django_q_task_func', task.get('func', ''))
            sentry_sdk.capture_exception(error=error)


