from parser import pars_inputs


def main():
    while True:
        user_input = input('>>> ').lower()
        output = pars_inputs(user_input)
        print(output)
        if output == 'Good bye!':
            exit()


if __name__ == '__main__':
    main()
