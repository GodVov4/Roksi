from collections import UserDict
from random import choice
from prints import WELCOME, HELP


def hello():
    return f'{choice(WELCOME)} My name is Roksi. {choice(HELP)}'


def goodbye():
    return 'Good bye!'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: str, phone=None, *_):
        self.name = Name(value=name.capitalize())
        self.phones = []
        if Phone(phone):
            self.add_phone_number(Phone(phone))

    def add_phone_number(self, phone: Phone) -> None:
        self.phones.append(phone)

    def del_phone(self, phone: str) -> None:
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def change_phone(self, phone: str) -> str:
        while self.phones:
            change = input(f'Contact "{self.name.value}" stores numbers '
                           f'{[i.value for i in self.phones]}. What number do I need to change? ')
            if change in [i.value for i in self.phones]:
                self.del_phone(change)
                break
            return 'Number does not exist.'
        else:
            return f'The contact has no numbers.'
        self.add_phone_number(Phone(phone))
        return f'Contact "{self.name.value}" changed.'


class AddressBook(UserDict):
    def add_record(self, record: Record) -> str:
        if record.name.value in self.data.keys():
            self.data[record.name.value].phones.extend(record.phones)
            return f'A number has been added to the contact "{record.name.value}".'
        else:
            self.data[record.name.value] = record
            return f'Contact "{record.name.value}" added.'

    def change_phone(self, record: Record) -> str:
        if data_record := self.data.get(record.name.value):
            return data_record.change_phone(record.phones[0].value)
        else:
            return f'Contact "{record.name.value}" not found'

    def get_phones(self, record: Record) -> str:
        if self.data.get(record.name.value):
            return (f'Contact "{record.name.value}" '
                    f'have numbers: {[i.value for i in self.data[record.name.value].phones]}.')
        return 'Contact not found.'

    def show_all(self) -> str:
        data = {}
        for k, v in self.data.items():
            data[k] = [i.value for i in v.phones]
        return f'Address book: {data}.'

    def del_phone(self, record: Record) -> str:
        del self.data[record.name.value]
        return f'Contact "{record.name.value}" deleted.'


address_book = AddressBook()


# def input_error(func):
#     def errors_catcher(command):
#         try:
#             function = func(command)
#         except (IndexError, KeyError, ValueError):
#             if func.__name__ == 'pars_inputs':
#                 return 'Command not found'
#             elif func.__name__ in ['add', 'change']:
#                 return 'Give me name and phone please'
#             elif func.__name__ == 'phone':
#                 return 'Enter user name'
#         else:
#             return function
#     return errors_catcher
#
