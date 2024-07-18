import pytest

import DATA
from test_main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book


@pytest.fixture
def correct_pair(book):
    book.add_new_book(DATA.CORRECT_NAMES[0])
    book.set_book_genre(DATA.CORRECT_NAMES[0], book.genre[0])
    return book.set_book_genre(DATA.CORRECT_NAMES[0], book.genre[0])


@pytest.fixture
def complex_data(book):
    book.add_new_book('Детское кино - 1')
    book.set_book_genre('Детское кино - 1', 'Фантастика')
    book.add_new_book('НЕ Детское кино - 1')
    book.set_book_genre('НЕ Детское кино - 1', 'Ужасы')
    book.add_new_book('НЕ Детское кино - 2')
    book.set_book_genre('НЕ Детское кино - 2', 'Детективы')
    book.add_new_book('Детское кино - 2')
    book.set_book_genre('Детское кино - 2', 'Мультфильмы')
    book.add_new_book('Детское кино - 3')
    book.set_book_genre('Детское кино - 3', 'Комедии')
    book.add_new_book('НЕ Детское кино - 3')
    book.set_book_genre('НЕ Детское кино - 3', 'Ужасы')
    book.add_new_book('НЕ Детское кино - 4')
    book.set_book_genre('НЕ Детское кино - 4', 'Детективы')
