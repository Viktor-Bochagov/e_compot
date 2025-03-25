import pytest

from src.category import Category
from src.product import Product


def test_category_init(category_phone, product_iphone, product_huawei):
    assert category_phone.name == "Смартфоны"
    assert category_phone.description == "Умные телефоны"
    assert category_phone.products_in_list == [product_iphone, product_huawei]

    assert category_phone.category_count == 1
    assert category_phone.product_count == 2


def test_categories_str_property(product_iphone, product_huawei):
    category = Category("Смартфоны", "Описание", [product_iphone, product_huawei])
    assert category.products == "iPhone 15 Pro Max, 200000 руб. Остаток: 20 шт.Huawei 7S, 30000 руб. Остаток: 14 шт."


def test_add_product(product_iphone, product_huawei):
    Category.product_count = 0
    Category.category_count = 0
    category = Category("Смартфоны", "Современные смартфоны", [product_iphone])

    assert category.product_count == 1
    assert category.category_count == 1

    category.add_product(product_huawei)

    assert category.product_count == 2
    assert category.category_count == 1

    assert product_huawei in category.products_in_list
    assert product_iphone in category.products_in_list


def test_category_str(category_phone):
    assert str(category_phone) == "Смартфоны, количество продуктов: 34 шт."


def test_category_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "iPhone 15 Pro Max"
    assert product_iterator.index == 1
    assert next(product_iterator).name == "Huawei 7S"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_add_product_error(product_iphone):
    category = Category("Смартфоны", "Современные смартфоны", [product_iphone])
    with pytest.raises(TypeError):
        category.add_product("Продукт другой категории")


def test_middle_price(category_zero_products):
    assert len(category_zero_products.products) == 0
    assert category_zero_products.middle_price() == 0

def test_middle_price_valid(category_phone):
    assert category_phone.middle_price() == 115000

def test_product_zero_quantity_raises_exception():
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Product("iPhone 13 Pro", "512Gb", 200000, 0)

def test_add_product_with_zero_quantity(capsys, category_phone):
    try:
        product_add = Product("iPhone 13 Pro", "512Gb", 200000, 0)
        category_phone.add_product(product_add)
    except ValueError as e:
        print(str(e))

    message = capsys.readouterr()
    assert 'Товар с нулевым количеством не может быть добавлен' in message.out
