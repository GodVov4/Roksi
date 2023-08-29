from collections import UserDict
from datetime import date
import re


class Iterator(UserDict):
    page_count = 0
    list_index = 0

    def __init__(self):
        super().__init__()
        self.number_of_records = 2

    def __next__(self) -> tuple:
        page = []
        Iterator.page_count += 1
        for index in range(Iterator.list_index, len(address_book.data)):
            page.append(
                list([name, [i.value for i in phone.phones]] for name, phone in address_book.data.items())[index]
            )
            Iterator.list_index += 1
            if len(page) == self.number_of_records or Iterator.list_index == len(address_book.data):
                break
        else:
            raise StopIteration
        return Iterator.page_count, page

    def __iter__(self):
        return self


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    @Field.value.setter
    def value(self, value) -> None:
        if len(value) < 20:
            self._value = value
        else:
            raise ValueError('Too long name.')


class Phone(Field):
    @Field.value.setter
    def value(self, value: str) -> None:
        if 9 <= len(value) <= 19 and re.match(r'[0-9+()-]', value):
            self._value = value
        else:
            raise ValueError("It's not a phone number.")


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str) -> None:
        if 6 <= len(value) <= 12 and re.match(r'[0-9./-]', value):
            self._value = value.replace('/', '.').replace('-', '.').replace(',', '.')
        else:
            raise ValueError('Incorrect birthday.')


class Record:
    def __init__(self, name: str, phone=None, birthday=None, *_):
        self.name = Name(value=name.capitalize())
        self.phones = []
        if phone:
            self.add_phone_number(phone)
        if birthday:
            self.birthday = Birthday(birthday)

    def add_phone_number(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def del_phone(self, phone: str) -> None:
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def change_phone(self, old_phone: str, new_phone: str) -> str:
        self.del_phone(old_phone)
        self.add_phone_number(new_phone)
        return f'Contact "{self.name.value}" changed.'

    def days_to_birthday(self) -> int | str:
        if self.birthday.value:
            date_list = [int(i) for i in self.birthday.value.split('.')[::-1]]
            if date_list[1:] > [date.today().month, date.today().day]:
                date_list[0] = date.today().year
            else:
                date_list[0] = date.today().year + 1
            delta = date(*date_list) - date.today()
            return f'There are {delta.days} days left until the birthday of contact "{self.name.value}".'
        else:
            raise f'Contact "{self.name.value}" does not have a birthday record'


class AddressBook(Iterator):
    def add_record(self, record: Record) -> str:
        if record.name.value in self.data:
            if hasattr(record, 'birthday'):
                if not hasattr(self.data.get(record.name.value), 'birthday'):
                    self.data.get(record.name.value).add_birthday(record.birthday.value)
                else:
                    return 'This contact already has a birthday'
            if record.phones[0].value in [phone.value for phone in self.data.get(record.name.value).phones]:
                return 'Contact already has this number'
            else:
                self.data.get(record.name.value).phones.extend(record.phones)
            return f'A number has been added to the contact "{record.name.value}".'
        else:
            self.data[record.name.value] = record
            return f'Contact "{record.name.value}" added.'

    def change_phone(self, name: str, old_phone: str, new_phone: str) -> str:
        data_record = self.data.get(name.capitalize())
        if not data_record:
            return f'Contact "{name.capitalize()}" no numbers'
        elif old_phone not in [i.value for i in data_record.phones]:
            return f'Contact "{name.capitalize()}" no number {old_phone}.'
        elif not new_phone:
            return 'Invalid format. Enter <name> <old number> <new number>.'
        elif data_record:
            return data_record.change_phone(old_phone, new_phone)
        else:
            return f'Contact "{name.capitalize()}" not found.'

    def get_phones(self, name: str) -> str:
        if name.capitalize() in self.data:
            if hasattr(self.data.get(name.capitalize()), 'birthday'):
                birth = self.data.get(name.capitalize()).birthday.value
            else:
                birth = 'not recorded'
            return (f'Contact "{name.capitalize()}" have numbers: '
                    f'{[i.value for i in self.data[name.capitalize()].phones]}, birthday {birth}.')
        return 'Contact not found.'

    # def show_all(self) -> str:
    #     data = {}
    #     for k, v in self.data.items():
    #         data[k] = [i.value for i in v.phones]
    #     return f'Address book: {data}.'

    def del_contact(self, name: str) -> str:
        del self.data[name.capitalize()]
        return f'Contact "{name.capitalize()}" deleted.'

    def iterator(self) -> str:
        for page_count, page in self:
            return (f'Address book:\nPage: {page_count}\n\n{page}\n\n'
                    f'Print "next" for show next page or "end" for close address book.') if page else 'End'

    def get_birthday(self, name: str) -> Record:
        return self.data.get(name.capitalize()).days_to_birthday()


address_book = AddressBook()
