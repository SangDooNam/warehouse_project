from warehouse import Warehouse, Product
from datetime import datetime as dt
from data.data import stock, personnel
from exceptions import get_integer, get_yes_no
from factory import Factory, Search
from personnel import Authentication

warehouse_list = Factory(mode="list")
warehouse_search = Factory(mode="search")


class Controller:
    """
    A class that serves as the main interface for user interaction within an inventory management system.

    This class is responsible for handling user inputs, displaying options, and managing the flow of the application.
    It allows users to perform various actions such as listing items by warehouse, searching for items, browsing items
    by category, and placing orders.

    Attributes:
        name (str): The name of the user interacting with the controller.
        option_dict (dict): A dictionary mapping numerical options to descriptive action strings.
        __authentication (bool): A flag indicating whether the user has been authenticated.
        select (dict): A dictionary of categories to browse, populated by __select().
        actions (list): A list of actions taken by the user during the session, used for session summary.

    Methods:
        get_name(): Prompts the user for their name.
        greeting(): Returns a greeting string for the user.
        options(): Displays available actions to the user and prompts for a choice.
        answers(): Processes user input and executes the corresponding actions.
        __list_item_by_warehouse(house_number, item_per_page): Lists items in a specified warehouse, with pagination.
        __search_item(search_term): Searches for items matching a search term and offers an option to place an order.
        __authenticated(): Authenticates the user with a username and password.
        __order(search_term, total_amount): Initiates the order process for a specified item.
        __browse(): Allows the user to browse items by category.
        __select(): Populates the select dictionary with categories from the inventory.
        __selected_category(category): Displays items in a specified category across all warehouses.
    """

    def __init__(self) -> None:
        self.name = None
        self.option_dict = {
            1: "List items by warehouse",
            2: "Search an item and place an order",
            3: "Browse by category",
            4: "Quit",
        }
        self.__authentication = False
        self.select = self.__select()
        self.actions = []

    def get_name(self):
        name = input("What is your name: ")
        self.name = name

    def greeting(self):
        return f"Hello, {self.name}. Welcome!"

    def options(self):
        for key, value in self.option_dict.items():
            print(f"{key}. {value}")
        print("What would you like to do?")
        self.prompt = "Type the number of the operation(1\\2\\3\\4): "
        start = self.answers()

    def answers(self):
        while True:
            answer = get_integer(self.prompt)
            if answer == 4:
                print(f"Thank you for your visit, {self.name}!")
                break

            elif answer not in list(self.option_dict.keys()):
                print(f"{answer} is not valid operation")
                continue

            elif answer == 1:
                house_number = get_integer(
                    f"Please select the house number of the warehouse(1 - {len(warehouse_list)}): "
                )
                if house_number <= len(warehouse_list) and house_number > 0:
                    action = self.__list_item_by_warehouse(house_number)
                    self.actions.append(action)
                else:
                    print(f"There is no warehouse {house_number}.")
                    continue

            elif answer == 2:
                search_term = input("Please type in the item you are looking for: ")
                action = self.__search_item(search_term.lower())
                if action:
                    self.actions.append(action)
            elif answer == 3:
                action = self.__browse()

    def __list_item_by_warehouse(self, house_number: int, item_per_page: int = 50):
        start_idx = 0
        counter = 1

        warehouse_stock = warehouse_list[house_number - 1].stock
        while start_idx * item_per_page < len(warehouse_stock):
            warehouse_stock.sort()
            start = start_idx * item_per_page
            end = start + item_per_page
            items_in_list = warehouse_stock[start:end]
            for item in items_in_list:
                print(f"{counter}. {item}")
                counter += 1
            print(f'Total {len(warehouse_stock)} items in "warehouse {house_number}"')
            next = input("Enter any key for next page or 'q' for quit: ")
            start_idx += 1
            if next == "q":
                return f"Listed {counter-1} items from warehouse {house_number}"
        return f"Listed {counter-1} items from warehouse {house_number}"

    def __search_item(self, search_term: str):
        warehouse_ids = warehouse_search.get_ids()
        lst = warehouse_search[0].stock
        lst.sort()
        results = Search(lst, search_term).results
        total_amount = len(results)
        if results:
            results = {
                key: [i for i in results if i.warehouse == key] for key in warehouse_ids
            }
            for key, value in results.items():
                for product in value:
                    date_of_stock = dt.strptime(
                        product.date_of_stock, "%Y-%m-%d %H:%M:%S"
                    )
                    date_of_stock = dt.now() - date_of_stock
                    print(
                        f"- {search_term.capitalize()} (in stock for {date_of_stock.days} days)"
                    )

                if len(value) == 1:
                    print(
                        f"In warehouse {key}, there is a total of {len(value)} {search_term}."
                    )
                elif len(value) > 1:
                    print(
                        f"In warehouse {key}, there is a total of {len(value)} {search_term}s."
                    )
            action = self.__order(search_term, total_amount)
            self.actions.append(action)
            return
        else:
            print(f"There is no {search_term}")
            return f"Searched for '{search_term.capitalize()}', but it was not found."

    def __authenticated(self):
        user_name = input("Please enter your user name: ")
        password = input("Enter the password: ")
        user = Authentication(user_name, password)
        if user.is_authenticated:
            self.__authentication = True
            return user.is_authenticated
        return user.is_authenticated

    def __order(self, search_term, total_amount):
        order_prompt = get_yes_no("Do you want to order this item? (y/n): ")
        if order_prompt == "n":
            return f"Searched a {search_term.capitalize()}"
        elif order_prompt == "y":
            if not self.__authentication:
                self.__authenticated()

            if self.__authentication:
                while True:
                    order_amount = get_integer(
                        f"How many would you like? (total amount:{total_amount}): "
                    )
                    if order_amount > 0 and order_amount <= total_amount:
                        if order_amount == 1:
                            print(
                                f"{order_amount} {search_term.capitalize()} has been ordered"
                            )
                            print(f"Thank you {self.name} for the order")
                            return f"Ordered a {search_term.capitalize()}"
                        else:
                            print(
                                f"{order_amount} {search_term.capitalize()}s have been ordered"
                            )
                            print(f"Thank you {self.name} for the order")
                            return f"Ordered {order_amount} {search_term.capitalize()}s"
                    else:
                        print(f"This amount '{order_amount}' is invalid for the order")
                        ask_one_more_time = input(
                            "Press any key to continue with your order, or press 'q' to quit: "
                        )
                        if ask_one_more_time == "q":
                            return f"Searched a {search_term.capitalize()}"
            else:
                print("You are not authenticated.")
                return f"Tried to place the order. but your authentication was denied."

    def __browse(self):
        for index, item_amount in self.select.items():
            print(f"{index}. {item_amount[0]} in amount {item_amount[1]}")
        select = get_integer("Type the number of the category to browse: ")
        if select in self.select:
            action = self.__selected_category(self.select[select][0])
            self.actions.append(action)
        else:
            print(f"There is not the number of the category: {select}")

    def __select(self):
        dictionary = {}
        items = warehouse_search[0].stock
        for item in items:
            category = item.category
            dictionary[category] = dictionary.get(category, 0) + 1
        dictionary = {
            idxs: (item_category, amount)
            for idxs, (item_category, amount) in enumerate(
                sorted(dictionary.items()), 1
            )
        }
        return dictionary

    def __selected_category(self, category):
        items_by_warehouse = warehouse_list
        browse = {}
        for warehouse in items_by_warehouse:
            browse.clear()
            for item in warehouse.stock:
                if item.category == category:
                    product = f"{item.state} {item.category}"
                    _, count = browse.get(product, (item.warehouse, 0))
                    browse[product] = (item.warehouse, count + 1)

            for key, value in browse.items():
                print(f"Quantity: {value[1]} | Type: {key}")
            print(f"- Warehouse {value[0]} Inventory: {category}")
            next = input("Enter any key for next warehouse or 'q' for quit: ")

            if next == "q":
                return f"Browsed {category}s"
        return f"Browsed {category}s"


if __name__ == "__main__":
    init = Controller()
    init.get_name()
    print(init.greeting())
    init.options()
    print("In this session you have:")
    for idx, i in enumerate(init.actions, 1):
        print(f"{idx}. {i}")
