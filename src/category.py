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

    def add_product(self, new_product: Product):
        """Метод для записи новых объектов класса Product в атрибут Category.products"""

        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products
