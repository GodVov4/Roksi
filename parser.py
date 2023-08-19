from handler import Record
from constants import COMMANDS


def input_error(func):
    def errors_catcher(*args, **kwargs):
        try:
            function = func(*args, **kwargs)
        except (KeyError, TypeError):
            return 'Command not found.'
        else:
            return function
    return errors_catcher


@input_error
def pars_inputs(command):
    command = command.strip()
    if command in COMMANDS.keys():
        return COMMANDS[command]()
    split_command = command.split()
    return COMMANDS[split_command[0]](Record(*split_command[1:]))
