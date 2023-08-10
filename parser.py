from handler import Record
from constants import COMMANDS
from handler import input_error


@input_error
def pars_inputs(command):
    command = command.strip()
    if command in COMMANDS.keys():
        return COMMANDS[command]()
    split_command = command.split()
    return COMMANDS[split_command[0]](Record(*split_command[1:]))
