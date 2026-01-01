from abc import ABC

class Media(ABC):
    def __init__(self, title, year):
        self.title = title
        self.year = year

class Book(Media):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

class Movie(Media):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director