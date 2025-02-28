class Category:
    """Класс для категорий товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация экземпляра класса Category. Задаем значения атрибутам экземпляра."""

        self.name = name
        self. description = description
        self. products = products
        Category.category_count += 1
        Category.product_count += len(products)
