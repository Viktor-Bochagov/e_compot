from src.category import Product


class Smartphone(Product):
    """ Класс, наследник класса Product. Описывает категорию товаров Смартфоны """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
