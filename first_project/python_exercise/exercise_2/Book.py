class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    ###getters###

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    ###setters###

    @title.setter
    def title(self, title):
        self.__title = title

    @author.setter
    def author(self, author):
        self.__author = author

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn
