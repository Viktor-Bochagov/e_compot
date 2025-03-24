class ZeroQuantityError(Exception):
    """
    Кастомное исключение, которое отвечает за обработку событий, когда в «Категорию» добавляется товар с нулевым количеством.
    """
    def __init__(self, message=None):
        super().__init__(message)
