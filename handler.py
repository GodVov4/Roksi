from random import choice
from prints import WELCOME, HELP


phone_book = {}


def input_error(func):
    def errors_catcher(command):
        try:
            function = func(command)
        except (IndexError, KeyError, ValueError):
            if func.__name__ == 'pars_inputs':
                return 'Command not found'
            elif func.__name__ in ['add', 'change']:
                return 'Give me name and phone please'
            elif func.__name__ == 'phone':
                return 'Enter user name'
        else:
            return function
    return errors_catcher


def hello():
    return f'{choice(WELCOME)} My name is Roksi. {choice(HELP)}'


@input_error
def add(keywords):
    if keywords[0].capitalize() in phone_book.keys():
        return f'Contact "{keywords[0].capitalize()}" already here'
    phone_book[keywords[0].capitalize()] = keywords[1]
    return f'Contact "{keywords[0].capitalize()}" added'


@input_error
def change(keywords):
    phone_book[keywords[0].capitalize()] = keywords[1]
    return f'Contact "{keywords[0].capitalize()}" changed'


@input_error
def phone(keywords):
    number = phone_book.get(keywords[0].capitalize(), 'Contact not found')
    return number


def show_all():
    return phone_book


def goodbye():
    return 'Good bye!'
