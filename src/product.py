class Product:
    """Класс для описания товаров, цены и имеющееся в наличии количество"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_of_product, list_of_products: list = []):
        """Метод для создания новых объектов класса Product. На вход необходимо подать словарь с параметрами товаров:
        name, description, price, quantity, а также текущий список товаров (для избежания дублирования позиций)"""

        for product in list_of_products:
            if dict_of_product['name'] == product.name:
                product.quantity += dict_of_product['quantity']
                if product.price < dict_of_product['price']:
                    product.price = dict_of_product['price']
                return product
        return cls(dict_of_product['name'], dict_of_product['description'], dict_of_product['price'],
                   dict_of_product['quantity'])

    @property
    def price(self):
        """Геттер для аттрибута price"""

        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Сеттер для изменения аттрибута price"""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            print("Вы собираетесь уменьшить цену на товар. Для подтверждения нажмите Y \n")
            confirmation = input()
            if confirmation.lower() != 'y':
                print("Цена не изменилась")
                return
            self.__price = new_price
