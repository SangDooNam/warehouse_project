def get_integer(prompt):
    """
    Prompts the user for input and ensures an integer is returned.

    This function repeatedly prompts the user for input until a valid integer is entered. If a non-integer
    value is entered, the user is informed and prompted again.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: The integer value entered by the user.
    """
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid value. Please type in integer.")


def get_yes_no(prompt):
    """
    Prompts the user for a yes or no response and ensures a valid response is returned.

    This function repeatedly prompts the user until a valid 'y' (yes) or 'n' (no) response is provided. It's case-insensitive
    and accepts 'y' and 'n' in any case (upper, lower, mixed).

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        str: The response entered by the user ('y' or 'n').
    """
    while True:
        answer = input(prompt).lower()
        if answer in ["y", "n"]:
            return answer
        else:
            print("Please type in 'y' or 'n'.")


class ArgumentMissingError(Exception):
    """
    Custom exception for handling missing arguments in function calls.

    This exception is raised when an expected argument is missing from a function or method call within the application.
    It's a more specific subclass of the Exception class, intended to provide clearer error messages related to argument issues.
    """

    pass
