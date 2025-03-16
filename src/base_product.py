from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, содержащий абстрактный метод для добавления новых продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
