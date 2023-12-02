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

class Warehouse:

    def __init__(self, warehouse_id:int) -> None:
        self.id = warehouse_id
        self.stock = []

    def order(self):
        pass

    def charge_stock(self, id):
        pass



for item in items:
    st = Product(**item)
    if st.warehouse == 1:
        print(len(item))











