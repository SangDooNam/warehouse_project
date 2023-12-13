from datetime import datetime
from data.data import stock as items


class Product:
    
    def __init__(self, state:str, category:str, warehouse:int, date_of_stock:datetime) -> None:
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock

    def __str__(self) -> str:
        return f'{self.state} {self.category}'

    def __repr__(self) -> str:
        return f'{self.state} {self.category}'
    
    def __lt__(self, other):
        if isinstance(other, str):
            return f'{self.state.lower()} {self.category.lower()}' < other
        return f'{self.state.lower()} {self.category.lower()}' < f'{other.state.lower()} {other.category.lower()}'
    
    def __eq__(self, other):
        if isinstance(other, str):
            return f'{self.state.lower()} {self.category.lower()}' == other
        return f'{self.state.lower()} {self.category.lower()}' == f'{other.state.lower()} {other.category.lower()}'
    
    def __gt__(self, other):
        if isinstance(other, str):
            return f'{self.state.lower()} {self.category.lower()}' > other
        return f'{self.state.lower()} {self.category.lower()}' > f'{other.state.lower()} {other.category.lower()}'
    
    def __getitem__(self, key):
        pass



class Warehouse:

    def __init__(self, warehouse_id:int) -> None:
        self.id = warehouse_id
        self.stock = []

    def add_product(self, mode) -> None:
        for item in items:
            if mode == 'list':
                if item['warehouse'] == self.id:
                    self.stock.append(Product(**item))
            elif mode == 'search':
                self.stock.append(Product(**item))
    
    
    def __str__(self) -> str:
        return f'Warehosue({self.id})'
    
    def __repr__(self) -> str:
        return f'Warehosue({self.id})'
    




