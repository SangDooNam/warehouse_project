

def get_integer(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print('Invalid value. Please type in integer.')