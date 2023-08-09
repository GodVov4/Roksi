from handler import *


COMMANDS = {
    'hello': hello,
    'hi': hello,
    'good bye': goodbye,
    'close': goodbye,
    'exit': goodbye,
    'show all': address_book.show_all,
    'phone': address_book.get_phones,
    'delete': address_book.del_phone,
    'add': address_book.add_record,
    'change': address_book.change_phone
}
