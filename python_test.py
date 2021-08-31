import pytest, sys
from db import load_from_db, save_to_db, flush_db
from repository import lib_repo
from helpers import sum

@pytest.mark.db
def test_save_to_db():
    data = {'a' : 1, 'b' : 2}
    result = save_to_db(data, db_name="test_db.json")
    assert result == True

@pytest.mark.db
def test_load_from_db():
    assert load_from_db("") == None
    assert bool(load_from_db("test_db.json")[0]) == True

@pytest.mark.repo
def test_get_book():
    source = load_from_db("test_db.json")
    book = lib_repo.get_book(source, "Lord of the Rings")
    assert bool(book) == True

@pytest.mark.parametrize("a,b", [[1,2], [3,4]])
def test_sum(a,b):
    assert sum(a,b) == a+b