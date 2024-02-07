from data.data import personnel


class User:
    """
    A class to represent a user in a system.

    This class provides basic functionalities for user representation including
    authentication status and name checking. It serves as a base class for more
    specialized types of users.

    Attributes:
        _name (str): The name of the user. Defaults to "Anonymous" if not provided.
        is_authenticated (bool): Indicates whether the user has been authenticated.

    Methods:
        authenticate(password): A placeholder method for user authentication,
                                always returns False in this base class.
        is_named(name): Checks if the user's name matches the provided name.
    """

    def __init__(self, user_name: str) -> None:
        self._name = user_name if user_name else "Anonymous"
        self.is_authenticated = False

    def authenticate(self, password: str) -> False:
        return False

    def is_named(self, name: str) -> bool:
        return self._name == name


class Employee(User):
    """
    A class to represent an employee, inheriting from User.

    This class extends the User class with additional attributes and methods specific to an employee,
    including authentication based on a password and management information.

    Attributes:
        __password (str): The employee's password for authentication purposes.
        head_of (list): A list of departments or teams the employee is head of. Can contain Employee instances.

    Methods:
        authenticate(password): Authenticates the employee by comparing the provided password
                                with the employee's password.
        __str__(): Returns the employee's name as a string representation.
        __repr__(): Returns an official string representation of the employee, including the name.

    Note:
        The head_of attribute is intended to represent a hierarchical structure within an organization,
        where an employee can be a manager of other Employee instances.
    """

    def __init__(self, user_name: str, password: str, head_of: list = None) -> None:
        super().__init__(user_name)
        self.__password = password
        self.head_of = [Employee(**employee) for employee in head_of] if head_of else []

    def authenticate(self, password: str) -> bool:
        if self.__password == password:
            self.is_authenticated = True
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self._name}"

    def __repr__(self) -> str:
        return f"{self._name}"


class Authentication:
    """
    A class to manage the authentication process for a list of employees.

    This class is responsible for authenticating a user based on a provided name and password. It initializes
    by collecting personnel information, presumably from a predefined list of employee data, and then attempts
    to validate the user against this list.

    Attributes:
        employees_list (list): A list of Employee instances representing the personnel information.
        is_authenticated (bool): Indicates whether the user has been successfully authenticated.

    Methods:
        __collect_personell_infos(): Collects and initializes personnel information into Employee instances.
                                     This method is intended to interact with a data source containing employee information.
        validate_user(): Validates the provided user name and password against the employees list.
        __check_password(employee, password): Recursively checks the provided password against the employee's
                                              password and the passwords of any employees under their supervision.
    """

    employees_list = None
    is_authenticated = None

    def __init__(self, name, password) -> None:
        self._name = name
        self.__password = password
        self.employees_list = self.__collect_personell_infos()
        self.is_authenticated = self.validate_user()

    def __collect_personell_infos(self):
        return [Employee(**person) for person in personnel]

    def validate_user(self):
        for employee in self.employees_list:
            if self.__check_password(employee, self.__password):
                return True
        return False

    def __check_password(self, employee, password):
        if employee._name == self._name and employee.authenticate(password):
            return True

        for baby_employee in employee.head_of:
            if self.__check_password(baby_employee, password):
                return True
        return False
