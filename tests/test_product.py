def test_product_init(product):
    assert product.name == "something"
    assert product.description == "useful tool for testing"
    assert product.price == 125.50
    assert product.quantity == 666
