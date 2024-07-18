import DATA
from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('correct_name', DATA.CORRECT_NAMES)
    def test_add_new_book_correct_input(self, book, correct_name):
        book.add_new_book(correct_name)
        assert correct_name in book.books_genre

    @pytest.mark.parametrize('incorrect_name', DATA.INCORRECT_NAMES)
    def test_add_new_book_incorrect_input(self, incorrect_name, book):
        book.add_new_book(incorrect_name)
        assert incorrect_name not in book.books_genre

    @pytest.mark.parametrize('name,genre', DATA.CORRECT_GENRES)
    def test_set_book_genre_add_existing_genre(self, book, name, genre):
        book.set_book_genre(name, genre)
        assert genre in book.genre

    @pytest.mark.parametrize('name,genre', DATA.INCORRECT_GENRES)
    def test_set_book_genre_add_non_existing_genre(self, book, name, genre):
        book.set_book_genre(name, genre)
        assert genre not in book.genre

    def test_set_book_genre_genre_update(self, book):
        book.add_new_book(DATA.CORRECT_NAMES[0])
        book.set_book_genre(DATA.CORRECT_NAMES[0], book.genre[0])
        temp_first_genre = book.books_genre[DATA.CORRECT_NAMES[0]]
        book.set_book_genre(DATA.CORRECT_NAMES[0], "Некорректный Жанр")
        temp_second_genre = book.books_genre[DATA.CORRECT_NAMES[0]]
        assert temp_first_genre == temp_second_genre


