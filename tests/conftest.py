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
def product():
    return Product("something", "useful tool for testing", 125.50, 666)
