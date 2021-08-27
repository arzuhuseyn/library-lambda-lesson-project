""" Python Unit tests / Test Driven Development """
from repository import lib_repo
from db import save_to_db, load_from_db

messages = {
    "welcome" : "Welcome to my Library 1.0!",
    "choose" : "Actions: - Create(1), -Update(2), -Search(3), - Delete(4) ",
}


print(messages["welcome"])

print(messages["choose"])
case = input("Please enter your choice: ")


if case == "1":
    category_name = input("Please enter the category name: ")
    author_name = input("Please enter the author name: ")
    author_surname = input("Please enter the author surname: ")
    author_nationality = input("Author nationality: ")
    book_name = input("Book Name: ")
    book_publication = input("Book Publication: ")

    category = lib_repo.create_category(name=category_name)
    author = lib_repo.create_author(name=author_name, surname=author_surname, nationality=author_nationality)
    book_item = lib_repo.create_book(
        name=book_name,
        publication=book_publication,
        category=category,
        author=author
    )
    saved = save_to_db(data=book_item.serialize())
    if saved:
        print("Congrats! Book saved to database")
    else:
        print("Sorry, something went wrong")
