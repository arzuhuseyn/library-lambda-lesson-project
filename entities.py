class Category:
    def __init__(self, name):
        self.name = name
 

class Author:
    def __init__(self, name, surname, nationality):
        self.name=name
        self.surname=surname
        self.nationality=nationality


class BookItem:
    def __init__(self, name, publication):
        self.name=name
        self.__category=None
        self.__author=None
        self.publication=publication

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, Category):
            raise TypeError('Invalid type of category')
        self.__category=value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError('Invalid type of author')
        self.__author=value

    def serialize(self):
        return {
            'name' : self.name,
            'category' : vars(self.category),
            'author' : vars(self.author),
            'publication' : self.publication
        }
