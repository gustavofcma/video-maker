from robots import user_input


def main():
    content = {}

    content['search_term'] = user_input.ask_and_return_search_term()
    content['prefix'] = user_input.ask_and_return_prefix()

    print(content)


if __name__ == '__main__':
    main()
