class Category:
    """Класс для категорий товаров"""

    name: str
    description: str
    products: list
    count_category = 0
    count_of_goods = 0


    def __init__(self, name, description, products):
        """Инициализация экземпляра класса Category. Задаем значения атрибутам экземпляра."""

        self.name = name
        self. description = description
        self. products = products
        Category.count_category += 1
        Category.count_of_goods += len(products)
