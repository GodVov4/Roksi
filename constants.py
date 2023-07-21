from handler import *


COMMANDS = {
    'hello': [0, hello],
    'hi': [0, hello],
    'add': [2, add],
    'change': [2, change],
    'phone': [1, phone],
    'show all': [0, show_all],
    'good bye': [0, goodbye],
    'close': [0, goodbye],
    'exit': [0, goodbye]
}
