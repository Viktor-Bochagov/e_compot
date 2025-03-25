from unittest.mock import patch

import pytest

from src.product import Product


def test_product_1_init(product_iphone):
    assert product_iphone.name == "iPhone 15 Pro Max"
    assert product_iphone.description == "1Tb"
    assert product_iphone.price == 200000
    assert product_iphone.quantity == 20


def test_product_2_init(product_huawei):
    assert product_huawei.name == "Huawei 7S"
    assert product_huawei.description == "512Gb"
    assert product_huawei.price == 30000
    assert product_huawei.quantity == 14


def test_price_property(product_iphone):
    assert product_iphone.price == 200000


def test_new_product(new_product_valid_1, new_product_valid_2, new_product_valid_3):
    products = []
    new_product = Product.new_product(new_product_valid_1, products)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product = Product.new_product(new_product_valid_2, products)
    assert new_product.name == "iPhone 15"
    assert len(products) == 0
    new_product = Product.new_product(new_product_valid_3, products)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert len(products) == 0
    assert new_product.quantity == 3


def test_price_update(product_iphone):
    with patch("builtins.input", side_effect=["y"]):
        product_iphone.price = 190000
        assert product_iphone.price == 190000


def test_price_update_invalid(product_iphone):
    with patch("builtins.print") as mocked_print:
        product_iphone.price = 0
        mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")


def test_product_str(product_iphone):
    assert str(product_iphone) == "iPhone 15 Pro Max, 200000 руб. Остаток: 20 шт."


def test_product_add(product_iphone, product_huawei):
    assert product_iphone + product_huawei == 4420000


def test_products_add(smartphone, smartphone_2):
    assert smartphone + smartphone_2 == 1334000.0


def test_products_add_invalid(smartphone, lawngrass):
    with pytest.raises(TypeError):
        assert smartphone + lawngrass


def test_products_add_invalid_else(smartphone_2, lawngrass_2):
    with pytest.raises(TypeError):
        assert smartphone_2 + lawngrass_2


def test_products_add_invalid_else_2(smartphone):
    with pytest.raises(TypeError):
        assert smartphone + 3


def test_zero_quantity_product():
    with pytest.raises(ValueError) as exc_info:
        Product("Huawei 8S", "32Gb", 15000, 0)
        assert str(exc_info.value) == 'Товар с нулевым количеством не может быть добавлен'
