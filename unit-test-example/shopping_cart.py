from typing import List
from item_database import ItemDatabase


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, ItemDatabase):
        total_price = 0.0
        for item in self.items:
            total_price += ItemDatabase.get(item)
        return total_price
