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
    def __init__(self, name: str, phone=None, new_phone=None, *_):
        self.name = Name(value=name.capitalize())
        self.phones = []
        if phone:
            self.add_phone_number(phone)
        self.new_phone = Phone(new_phone)

    def add_phone_number(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def del_phone(self, phone: str) -> None:
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def change_phone(self, old_phone: str, new_phone: str) -> str:
        self.del_phone(old_phone)
        self.add_phone_number(new_phone)
        return f'Contact "{self.name.value}" changed.'


class AddressBook(UserDict):
    def add_record(self, record: Record) -> str:
        if record.name.value in self.data.keys():
            if self.data[record.name.value].phones == [None]:
                self.data[record.name.value] = record
            else:
                self.data[record.name.value].phones.extend(record.phones)
            return f'A number has been added to the contact "{record.name.value}".'
        else:
            self.data[record.name.value] = record
            return f'Contact "{record.name.value}" added.'

    def change_phone(self, record: Record) -> str:
        data_record = self.data.get(record.name.value)
        if not record.new_phone.value:
            return 'Invalid format. Enter <name> <old number> <new number>.'
        elif record.phones[0].value not in [i.value for i in data_record.phones]:
            return f'Contact {record.name.value} no number {record.phones[0].value}.'
        elif data_record:
            return data_record.change_phone(record.phones[0].value, record.new_phone.value)
        else:
            return f'Contact "{record.name.value}" not found.'

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
