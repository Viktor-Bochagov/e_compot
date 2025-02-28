def test_category_init(first_category, second_category):
    assert first_category.name == "test"
    assert first_category.description == "testing category"
    assert len(first_category.products) == 2

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_of_goods == 4
    assert second_category.count_of_goods == 4
