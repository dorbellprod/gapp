CLEAR = "\u001b[0m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"

def print_error(contents):
    print(RED, end='')
    print(contents)
    print(CLEAR, end='')

def print_success(contents):
    print(GREEN, end='')
    print(contents)
    print(CLEAR, end='')
