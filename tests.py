import unittest
from entities import Category, Author, BookItem
from repository import lib_repo
from db import save_to_db, load_from_db, flush_db


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.author = lib_repo.create_author(
            name="Artur",
            surname="Conan Doyle",
            nationality="english"
        )
        self.category = lib_repo.create_category(
            name="Detective"
        )
        self.book_item = lib_repo.create_book(
            name="Sherlock Holmes",
            author=self.author,
            category=self.category,
            publication="Queen`s"
        )
        self.book_saved = save_to_db(self.book_item.serialize(), db_name="test_db.json")
        self.db = load_from_db(db_name="test_db.json")
        return super().setUp()

    def test_create_author(self):
        self.assertIsInstance(self.author, Author)
        self.assertEqual(self.author.name, "Artur")
        self.assertEqual(self.author.surname, "Conan Doyle")
        self.assertEqual(self.author.nationality, "english")

    def test_create_category(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.name, "Detective")

    def test_create_book_item(self):
        self.assertIsInstance(self.book_item, BookItem)
        self.assertIsInstance(self.book_item.category, Category)
        self.assertIsInstance(self.book_item.author, Author)
        self.assertEqual(self.book_item.name, "Sherlock Holmes")
        self.assertEqual(self.book_item.author.name, "Artur")
        self.assertEqual(self.book_item.category.name, "Detective")
        self.assertEqual(self.book_item.publication, "Queen`s")

    def test_save_to_db(self):
        self.assertEqual(self.book_saved, True)
    
    def test_load_from_db(self):
        for item in self.db:
            self.assertEqual(item["name"], "Sherlock Holmes")
            self.assertEqual(item["author"]["name"], "Artur")
            self.assertEqual(item["category"]["name"], "Detective")
            self.assertEqual(item["publication"], "Queen`s")
    
    def tearDown(self) -> None:
        flush_db(db_name="test_db.json")
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()