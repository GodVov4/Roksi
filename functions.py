from random import choice
from prints import WELCOME, HELP
from handler import *


def start() -> str:
    return f'{choice(WELCOME)} My name is Roksi. {choice(HELP)}'


def end() -> str:
    return 'Good bye!'


def add(name: str, phone=None, birthday=None) -> AddressBook:
    return address_book.add_record(Record(name, phone, birthday))


def get_all() -> AddressBook:
    end_iterator()
    return address_book.iterator()


def next_page() -> AddressBook | str:
    page = address_book.iterator()
    return 'End' if page is None else page


def end_iterator() -> str:
    Iterator.page_count = 0
    Iterator.list_index = 0
    return 'Address book closed'


def get_birthday(name: str) -> str:
    return address_book.get_birthday(name)


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
    'next': next_page,
    'end': end_iterator,
    'birthday': get_birthday,
    'phone': get_phone,
    'change': change,
    'delete': delete,
}
