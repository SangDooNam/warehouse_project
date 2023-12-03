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
        return f'{self.state} {self.category}' < f'{other.state} {other.category}'
    
    def __eq__(self, other):
        return f'{self.state} {self.category}' < f'{other.state} {other.category}'

class Warehouse:

    def __init__(self, warehouse_id:int) -> None:
        self.id = warehouse_id
        self.stock = []

    def order(self):
        pass

    def add_product(self) -> None:
        for item in items:
            if item['warehouse'] == self.id:
                self.stock.append(Product(**item))
        


    

import random


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heap(arr):
    n = len(arr)

    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)
    for i in range(n -1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

warehouse = Warehouse(2)
warehouse.add_product()

print(heap(warehouse.stock))





