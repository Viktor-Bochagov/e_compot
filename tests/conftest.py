import pytest

from src.category import Category
from src.lawngrass_category import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone_category import Smartphone


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


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass():
    return LawnGrass("Газонная трава", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Газонная трава 2", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
