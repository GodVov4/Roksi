from random import choice
from prints import WELCOME, HELP
from handler import *


def start() -> str:
    return f'{choice(WELCOME)} My name is Roksi. {choice(HELP)}'


def end() -> str:
    return 'Good bye!'


def add(name: str, phone=None) -> AddressBook:
    if phone:
        return address_book.add_record(Record(name, phone))
    else:
        return address_book.add_record(Record(name))


def get_all() -> AddressBook:
    return address_book.show_all()


def get_phone(name: str) -> AddressBook:
    return address_book.get_phones(name)


def change(name: str, old_phone: str, new_phone: str) -> AddressBook:
    return address_book.change_phone(name, old_phone, new_phone)


def delete(name: str) -> AddressBook:
    return address_book.del_contact(name)


COMMANDS = {
    'hello': start,
    'hi': start,
    'good bye': end,
    'close': end,
    'exit': end,
    'add': add,
    'show all': get_all,
    'phone': get_phone,
    'change': change,
    'delete': delete,
}
