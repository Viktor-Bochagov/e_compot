def test_print_mixin(capsys, product_iphone):
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(iPhone 15 Pro Max, 1Tb, 200000, 20)'


def test_print_mixin_smartphone(capsys, smartphone):
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)'


def test_print_mixin_lawngrass(capsys, lawngrass):
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газонная трава, Выносливая трава, 450.0, 15)'
