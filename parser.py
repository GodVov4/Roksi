from functions import COMMANDS


def input_error(func):
    def errors_catcher(*args, **kwargs):
        try:
            function = func(*args, **kwargs)
        except (TypeError, IndexError):
            return 'Incorrect command.'
        except ValueError as too_long:
            return too_long
        else:
            return function
    return errors_catcher


@input_error
def pars_inputs(command):
    command = command.strip()
    if command in COMMANDS.keys():
        return COMMANDS.get(command)()
    split_command = command.split()
    return COMMANDS.get(split_command[0])(*split_command[1:])
