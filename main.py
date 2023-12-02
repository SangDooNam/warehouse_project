from warehouse import Warehouse, Product
from data.data import stock, personnel

class Initialize:

    def __init__(self) -> None:
        self.name = None
        self.option_dict = {
                            1: "List items by warehouse", 
                            2: 'Search an item and place an order', 
                            3: 'Browse by category', 
                            4: 'Quit'
                            }
        self.yes_no = ['yes', 'no']

    def get_name(self):
        name = input("What is your name: ")
        self.name = name

    def greeting(self):
        return f'Hello, {self.name}. Welcome!'

    def options(self):
        for key, value in self.option_dict.items():
            print(f'{key}. {value}')
        print("What would you like to do?")
        self.prompt = ('Type the number of the operation(1\\2\\3\\4):')
        start = self.answers()

    def answers(self):
        while True:
            answer = input(self.prompt)
            if answer == "4":
                print(f"Thank you for your visit, {self.name}!")
                break

            elif answer not in list(ini.option_dict.keys()):
                print(f"{answer} is not valid operation")
                continue
            
            elif answer == "1":
                pass
            elif answer == "2":
                pass
            elif answer == "4":
                pass

    def list_item_by_warehouse(self, house_number:int, item_per_page:int=50):
        for item in stock:
            product = Product(**item)
            if item["warehouse"] == house_number:

        
        
        



if __name__ == '__main__':
    ini = Initialize()
    ini.get_name()
    print(ini.greeting())
    ini.options()
