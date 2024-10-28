import pytest
from typing import Dict, List
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    name: str
    price: Decimal
    stock: int


class ProductDatabase:
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, name: str, price: Decimal, stock: int):
        self.products[name] = Product(name=name, price=price, stock=stock)

    def get_product(self, name: str) -> Product:
        return self.products[name]


class ShoppingCart:
    def __init__(self, product_db: ProductDatabase):
        self.items: Dict[str, int] = {}
        self.product_db = product_db

    def add_item(self, item: str, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        product = self.product_db.get_product(item)
        if product.stock < quantity:
            raise ValueError(f"Not enough {item} in stock")
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


@pytest.fixture
def product_db():
    db = ProductDatabase()
    db.add_product("apple", Decimal("0.50"), 100)
    db.add_product("banana", Decimal("0.30"), 50)
    db.add_product("orange", Decimal("0.60"), 75)
    return db


@pytest.fixture
def cart(product_db):
    return ShoppingCart(product_db)


@pytest.fixture
def filled_cart(cart):
    cart.add_item("apple", 3)
    cart.add_item("banana", 2)
    return cart


def test_add_item(cart):
    cart.add_item("apple", 3)
    assert cart.items["apple"] == 3


def test_remove_item(filled_cart):
    filled_cart.remove_item("banana", 1)
    assert filled_cart.items["banana"] == 1


def test_add_out_of_stock(cart):
    with pytest.raises(ValueError, match="Not enough orange in stock"):
        cart.add_item("orange", 100)
