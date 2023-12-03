from warehouse import Warehouse, Product
from data.data import stock, personnel
from exceptions import get_integer

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
            answer = get_integer(self.prompt)
            if answer == 4:
                print(f"Thank you for your visit, {self.name}!")
                break

            elif answer not in list(ini.option_dict.keys()):
                print(f"{answer} is not valid operation")
                continue
            
            elif answer == 1:
                house_number = get_integer('which warehouse: ')
                self.list_item_by_warehouse(house_number)
            elif answer == 2:
                pass
            elif answer == 3:
                pass

    def list_item_by_warehouse(self, house_number:int, item_per_page:int=50):
        warehouse = Warehouse(house_number)
        warehouse.add_product()
        start_idx = 0
        counter = 1
        if warehouse.stock:
            while start_idx * item_per_page < len(warehouse.stock):
                start = start_idx * item_per_page
                end = start + item_per_page
                items_in_list = warehouse.stock[start:end]
                for item in items_in_list:
                    print(f'{counter}. {item}')
                    counter += 1
                next = input("Enter any key for next page or 'q' for quit: ")
                start_idx += 1
                if next == 'q':
                    break
        else:
            print(f'There is no item in warehouse {house_number}')

if __name__ == '__main__':
    ini = Initialize()
    ini.get_name()
    print(ini.greeting())
    ini.options()
