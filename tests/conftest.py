import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def product_iphone():
    return Product("iPhone 15 Pro Max", "1Tb", 200000, 20)

@pytest.fixture
def product_huawei():
    return Product("Huawei 7S", "512Gb", 30000, 14)

@pytest.fixture
def category_phone(product_huawei, product_iphone):
    return Category("Смартфоны", "Умные телефоны", [product_iphone, product_huawei])

@pytest.fixture
def new_product_valid_1():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

@pytest.fixture
def new_product_valid_2():
    return {"name": "iPhone 15", "description": "256GB, Серый цвет", "price": 210000, "quantity": 3}


@pytest.fixture
def new_product_valid_3():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 3,
    }


@pytest.fixture
def product_iterator(category_phone):
    return ProductIterator(category_phone)
