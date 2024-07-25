import pytest

import DATA
from tests import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book


@pytest.fixture
def complex_data(book):
    for textbook in DATA.BOOK_LIST:
        book.add_new_book(textbook)
    for textbook in DATA.BOOK_LIST:
        index = DATA.BOOK_LIST.index(textbook)
        book.set_book_genre(textbook, book.genre[index])
