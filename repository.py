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

    # From pytest lesson
    def get_book(self, source, name):
        book = list(filter(lambda x: x.get('name') == name, source))
        if book:
            author = self.create_author(**book[0]['author'])
            category = self.create_category(**book[0]['category'])
            return self.create_book(book[0]['name'], author, category, book[0]['publication'])
        return None

    

 
lib_repo = LibraryRepository()