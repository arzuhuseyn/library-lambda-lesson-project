from entities import Category, Author, BookItem


class LibraryRepository:

    def create_author(self, name, surname, nationality):
        return Author(name=name, surname=surname, nationality=nationality)

    def create_category(self, name):
        return Category(name=name)

    def create_book(self, name, author, category, publication):
        instance = BookItem(name=name, publication=publication)
        instance.author = author
        instance.category = category
        return instance


lib_repo = LibraryRepository()