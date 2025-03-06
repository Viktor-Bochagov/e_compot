class ProductIterator:
    """ Класс, с помощью которого можно перебирать товары одной категории,
    метод выполнения следующего шага итерации возвращает очередной товар категории"""

    def __init__(self, category_obj):
        """Инициализирует итератор"""

        self.category_obj = category_obj
        self.index = 0

    def __iter__(self):
        """Возвращает итератор"""

        self.index = 0
        return self

    def __next__(self):
        """Возвращает объект Category - следующий продукт в списке"""

        if self.index < len(self.category_obj.products_in_list):
            product = self.category_obj.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
