import parser


def main():
    while True:
        user_input = input('>>> ').lower()
        output, close = parser.pars_inputs(user_input)
        print(output)
        if close:
            exit()


if __name__ == '__main__':
    main()
