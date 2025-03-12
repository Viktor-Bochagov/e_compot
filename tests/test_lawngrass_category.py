def test_lawngrass_init(lawngrass):
    assert lawngrass.name == "Газонная трава"
    assert lawngrass.description == "Выносливая трава"
    assert lawngrass.price == 450.0
    assert lawngrass.quantity == 15
    assert lawngrass.country == "США"
    assert lawngrass.germination_period == "5 дней"
    assert lawngrass.color == "Темно-зеленый"
