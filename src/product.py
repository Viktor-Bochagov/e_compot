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

    def __str__(self):
        """Выводит строковое отображение в заданном формате"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Складывает стоимость товаров определенной категории на складе"""
        if type(self) is type(other):
            return (self.quantity * self.__price) + (other.quantity * other.__price)

        raise TypeError

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

    @classmethod
    def new_product(cls, dict_of_product, list_of_products):
        """Метод для создания новых объектов класса Product. На вход необходимо подать словарь с параметрами товаров:
        name, description, price, quantity, а также текущий список товаров (для избежания дублирования позиций)"""

        name = dict_of_product.get("name")
        description = dict_of_product.get("description")
        price = dict_of_product.get("price")
        quantity = dict_of_product.get("quantity")

        for product in list_of_products:
            if product.name == name:
                product.price = max(price, product.price)
                product.quantity += quantity
                return product

        dict_product = cls(name, description, price, quantity)
        list_of_products.append(dict_of_product)
        return dict_product
