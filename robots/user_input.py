import pyinputplus as pyip

def ask_and_return_search_term():
    return pyip.inputStr(prompt='Type a Wikipedia search term: ')


def ask_and_return_prefix():
    prefixes = [
        'Who is',
        'What is',
        'The history of',
        'CANCEL',
    ]

    return pyip.inputMenu(choices=prefixes, numbered=True, prompt='Choose a prefix for the search:\n')


def main():
    pass
