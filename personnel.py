from data.data import personnel


class User:
    
    def __init__(self, user_name:str) -> None:
        self._name = user_name if user_name else "Anonymous"
        self.is_authenticated = False
        
    
    def authenticate(self, password:str) -> False:
        return False
    
    def is_named(self, name:str) -> bool:
        return self._name == name
    


class Employee(User):
    
    def __init__(self, user_name: str, password:str, head_of:list=None) -> None:
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
        return f'{self._name}'

    def __repr__(self) -> str:
        return f'{self._name}'



class Authentication:
    
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

