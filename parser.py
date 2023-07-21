from constants import COMMANDS
from handler import input_error


@input_error
def pars_inputs(command):
    command = command.strip()
    if command in COMMANDS.keys() and not COMMANDS[command][0]:
        return COMMANDS[command][1]()
    split_command = command.split()
    return COMMANDS[split_command[0]][1](split_command[1:])
