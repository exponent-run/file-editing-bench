import pytest
from typing import Dict, List

class ShoppingCart:
    def __init__(self):
        self.items: Dict[str, int] = {}
        
    def add_item(self, item: str, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items[item] = self.items.get(item, 0) + quantity
    
    def remove_item(self, item: str, quantity: int = 1):
        if item not in self.items:
            raise KeyError(f"Item {item} not in cart")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.items[item] < quantity:
            raise ValueError("Not enough items in cart")
        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 3)
    assert cart.items["apple"] == 3

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("banana", 2)
    cart.remove_item("banana", 1)
    assert cart.items["banana"] == 1