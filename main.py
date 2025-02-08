class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # защита атрибута названия книги
        self._author = author  # защита автора книги

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга \"{self.name}\". Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # инициализация через свойство

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целочисленно.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  #инициализация через свойство

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом с плавающей запятой.")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}. Продолжительность аудиокниги: {self.duration:.2f} ч."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == '__main__':
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    print(paper_book)
    print(repr(paper_book))

    print(audio_book)
    print(repr(audio_book))
