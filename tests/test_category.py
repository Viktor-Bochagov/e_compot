def test_category_init(first_category, second_category):
    assert first_category.name == "test"
    assert first_category.description == "testing category"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_add_product(third_category, product):
    assert third_category.product_count == 6
    third_category.add_product(product)
    assert third_category.product_count == 7
    assert third_category.products == ('everything, 69.77 руб. Остаток: 13 шт.\n'
                                        'nothing, 100 руб. Остаток: 34435353 шт.\n'
                                        'something, 125.5 руб. Остаток: 666 шт.\n')


def test_products_getter(second_category):
    assert second_category.products == ('everything, 69.77 руб. Остаток: 13 шт.\n'
                                        'nothing, 100 руб. Остаток: 34435353 шт.\n')