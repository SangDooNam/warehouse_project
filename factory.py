from data.data import stock as items
from warehouse import Warehouse, Product
from exceptions import ArgumentMissingError


class Factory:
    """
    A class to manage and operate on warehouses and their inventories.

    The Factory class is designed to handle various operations related to warehouses,
    such as listing warehouse information, searching through warehouses, and managing
    warehouse inventories based on the operational mode set during instantiation.

    Attributes:
        mode (str): Operational mode of the Factory, determining the behavior of certain methods.
        container (list): Holds the list of Warehouse objects or search results.
        warehouse_ids (list): List of unique warehouse IDs managed by the Factory.

    Methods:
        parse(): Parses warehouse data based on the current mode.
        get_ids(): Retrieves and returns a list of unique warehouse IDs.
        warehouse_in_list(mode): Generates a list of Warehouse objects based on the mode.
        __iter__(): Allows iteration over the Factory's container.
        __getitem__(key): Enables index-based access to the Factory's container.
        __len__(): Returns the number of items in the Factory's container.
    """

    mode = None
    container = None

    def __init__(self, *args, **kwargs) -> None:
        self.warehouse_ids = []
        if "mode" not in kwargs:
            raise ArgumentMissingError("The key argument must include 'mode' as a key.")
        self.mode = kwargs["mode"]
        self.parse()

    def parse(self):
        if self.mode == "list":
            self.container = self.warehouse_in_list(self.mode)
        elif self.mode == "search":
            self.container = self.warehouse_in_list(self.mode)

    def __get_warehouse_ids(self):
        if self.warehouse_ids:
            return self.warehouse_ids
        for item in items:
            if item["warehouse"] not in self.warehouse_ids:
                self.warehouse_ids.append(item["warehouse"])

        return self.warehouse_ids

    def get_ids(self):
        return self.__get_warehouse_ids()

    def warehouse_in_list(self, mode):
        warehouse_list = []
        self.warehouse_ids = self.__get_warehouse_ids()
        if mode == "list":
            for id in self.warehouse_ids:
                warehouse_list.append(Warehouse(id))
            for warehouse in warehouse_list:
                warehouse.add_product(mode)
        elif mode == "search":
            warehouse_list.append(Warehouse(1))
            warehouse_list[0].add_product(mode)

        return warehouse_list

    def __iter__(self, *args, **kwargs):
        yield from self.container

    def __getitem__(self, key):
        return self.container[key]

    def __len__(self):
        return len(self.container)


class Search:
    """
    A class to perform search operations within a list to find all occurrences of a search term.

    The Search class is designed to efficiently find the range of indices for a given search term
    within a sorted list using a modified binary search algorithm. Upon initialization, it performs
    the search and stores the result.

    Attributes:
        results (list): The list of items matching the search term found within the input list.
                        This is empty if the term is not found.

    Methods:
        __front_index(lst, search_term): Finds the index of the first occurrence of the search term
                                         in the list.
        __end_index(lst, search_term): Finds the index of the last occurrence of the search term
                                       in the list.
        __search_items(lst, search_term): Uses __front_index and __end_index to find and store
                                          all occurrences of the search term in 'results'.
    """

    results = None

    def __init__(self, lst: list, search_term: str) -> None:
        self.__search_items(lst, search_term)

    def __front_index(self, lst: list, search_term: str):
        left = 0
        right = len(lst) - 1
        result = -1

        while right >= left:
            middle = (right + left) // 2

            if lst[middle] == search_term:
                result = middle
                right = middle - 1

            elif lst[middle] > search_term:
                right = middle - 1

            else:
                left = middle + 1

        return result

    def __end_index(self, lst: list, search_term: str):
        left = 0
        right = len(lst) - 1
        result = -1

        while right >= left:
            middle = (right + left) // 2

            if lst[middle] == search_term:
                result = middle
                left = middle + 1

            elif lst[middle] > search_term:
                right = middle - 1

            else:
                left = middle + 1

        return result

    def __search_items(self, lst: list, search_term: str):
        front_idx = self.__front_index(lst, search_term)
        end_idx = self.__end_index(lst, search_term)

        if front_idx != -1 and end_idx != 1:
            self.results = lst[front_idx : end_idx + 1]
        else:
            self.results = []
