from src.product import Product


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
        self.description = description
        self.__products = list(products)
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        full_count = 0
        for product in self.__products:
            full_count += product.quantity
        return f'{self.name}, количество продуктов: {full_count} шт.'

    def add_product(self, product):
        """Метод для записи новых объектов класса Product в атрибут Category.products"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}"
        return product_str

    @property
    def products_in_list(self):
        return self.__products
