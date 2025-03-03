import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category("test", "testing category", [
        Product("something", "useful tool for testing", 125.50, 666),
        Product("anything", "everything you desire", 9999999.99, 1)])


@pytest.fixture
def second_category():
    return Category("examination", "category for examination", [
        Product("everything", "everything everywhere and at once", 69.77, 13),
        Product("nothing", "respectfully accepting donations", 100, 34435353)])


@pytest.fixture
def third_category():
    return Category("some category", "category with something", [
        Product("everything", "everything everywhere and at once", 69.77, 13),
        Product("nothing", "respectfully accepting donations", 100, 34435353)])


@pytest.fixture
def product():
    return Product("something", "useful tool for testing", 125.50, 666)


@pytest.fixture
def product_in_dict():
    return {"name": "everything", "description": "everything everywhere and at once", "price": 69.77, "quantity": 13}


@pytest.fixture
def first_list_products():
    return [Product("anything", "everything you desire", 9999999.99, 1)]


@pytest.fixture
def second_list_products():
    return [Product("everything", "everything you desire", 9999999.99, 1)]


@pytest.fixture
def third_list_products():
    return [Product("everything", "everything you desire", 10.50, 1)]
