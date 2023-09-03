import pickle
import handler
from parser import pars_inputs


def write_file():
    filename = 'address_book.bin'
    with open(filename, 'wb') as file:
        pickle.dump(handler.address_book.data, file)


def main():
    while True:
        try:
            user_input = input('>>> ').lower()
        finally:
            write_file()
        output = pars_inputs(user_input)
        print(output)
        if output == 'Good bye!':
            write_file()
            exit()


if __name__ == '__main__':
    main()
