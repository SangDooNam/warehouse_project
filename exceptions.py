

def get_integer(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print('Invalid value. Please type in integer.')


def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ['y', 'n']:
            return answer
        else:
            print("Please type in 'y' or 'n'.")
            


class ArgumentMissingError(Exception):
    pass