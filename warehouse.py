from datetime import datetime
from data.data import stock as items


class Product:
    """
    A class to represent a product within an inventory management system.

    This class provides a structure for storing product information, including its
    state, category, associated warehouse, and the date it was stocked. It includes
    special methods to enable string representations and comparison operations based
    on the product's state and category.

    Attributes:
        state (str): The state of the product, e.g., 'New', 'Used'.
        category (str): The category to which the product belongs, e.g., 'Electronics'.
        warehouse (int): The identifier for the warehouse where the product is stored.
        date_of_stock (datetime): The date when the product was stocked in the warehouse.

    Special Methods:
        __str__(self): Returns a simple string representation of the product.
        __repr__(self): Returns an unambiguous string representation of the product.
        __lt__(self, other): Defines the behavior for the less-than operator (<).
        __eq__(self, other): Defines the behavior for the equality operator (==).
        __gt__(self, other): Defines the behavior for the greater-than operator (>).
        __getitem__(self, key): Placeholder method for item access, not implemented.

    The comparison operators allow `Product` instances to be compared to each other
    or to string representations, facilitating sorting and filtering based on the
    concatenated lowercase state and category strings.
    """

    def __init__(
        self, state: str, category: str, warehouse: int, date_of_stock: datetime
    ) -> None:
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock

    def __str__(self) -> str:
        return f"{self.state} {self.category}"

    def __repr__(self) -> str:
        return f"{self.state} {self.category}"

    def __lt__(self, other):
        if isinstance(other, str):
            return f"{self.state.lower()} {self.category.lower()}" < other
        return (
            f"{self.state.lower()} {self.category.lower()}"
            < f"{other.state.lower()} {other.category.lower()}"
        )

    def __eq__(self, other):
        if isinstance(other, str):
            return f"{self.state.lower()} {self.category.lower()}" == other
        return (
            f"{self.state.lower()} {self.category.lower()}"
            == f"{other.state.lower()} {other.category.lower()}"
        )

    def __gt__(self, other):
        if isinstance(other, str):
            return f"{self.state.lower()} {self.category.lower()}" > other
        return (
            f"{self.state.lower()} {self.category.lower()}"
            > f"{other.state.lower()} {other.category.lower()}"
        )

    def __getitem__(self, key):
        pass


class Warehouse:
    """
    A class to represent a warehouse in an inventory management system.

    This class provides functionalities to manage the stock of products in a warehouse.
    It allows adding products to the warehouse stock based on a specified mode of operation,
    such as listing all products for a given warehouse or adding products based on search criteria.

    Attributes:
        id (int): The unique identifier for the warehouse.
        stock (list): A list to hold the stock of products (Product instances) in the warehouse.

    Methods:
        add_product(mode): Adds products to the warehouse's stock based on the specified mode.
                           In 'list' mode, it adds products that match the warehouse's ID. In 'search' mode,
                           it adds products regardless of the warehouse ID.

    The string representation (__str__) and the official string representation (__repr__) of
    the Warehouse class both return a string that includes the warehouse ID, facilitating easy
    identification of Warehouse instances.
    """

    def __init__(self, warehouse_id: int) -> None:
        self.id = warehouse_id
        self.stock = []

    def add_product(self, mode) -> None:
        for item in items:
            if mode == "list":
                if item["warehouse"] == self.id:
                    self.stock.append(Product(**item))
            elif mode == "search":
                self.stock.append(Product(**item))

    def __str__(self) -> str:
        return f"Warehosue({self.id})"

    def __repr__(self) -> str:
        return f"Warehosue({self.id})"
