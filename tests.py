import DATA
from main import BooksCollector
import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('correct_name', DATA.BOOK_LIST)
    def test_add_new_book_correct_input(self, book, correct_name):
        book.add_new_book(correct_name)
        assert correct_name in book.books_genre

    @pytest.mark.parametrize('incorrect_name', DATA.INCORRECT_NAMES)
    def test_add_new_book_incorrect_input(self, incorrect_name, book):
        book.add_new_book(incorrect_name)
        assert incorrect_name not in book.books_genre

    def test_set_book_genre_add_existing_genre(self, book):
        book.add_new_book(DATA.BOOK_LIST[0])
        book.set_book_genre(DATA.BOOK_LIST[0], book.genre[0])
        assert list(book.books_genre.values())[0] in book.genre

    def test_set_book_genre_add_non_existing_genre(self, book):
        book.set_book_genre(DATA.BOOK_LIST[0], DATA.NON_EXISTING_GENRE)
        assert DATA.NON_EXISTING_GENRE not in book.genre

    def test_set_book_genre_genre_not_update_with_incorrect_data(self, book, complex_data):
        temp_first_genre = book.books_genre[DATA.BOOK_LIST[0]]
        book.set_book_genre(DATA.BOOK_LIST[0], DATA.NON_EXISTING_GENRE)
        temp_second_genre = book.books_genre[DATA.BOOK_LIST[0]]
        assert temp_first_genre == temp_second_genre

    def test_get_book_genre_return_correct_genre(self, book, complex_data):
        assert book.get_book_genre(DATA.BOOK_LIST[0]) == book.books_genre[DATA.BOOK_LIST[0]]

    def test_get_books_with_specific_genre_shows_selected_genre(self, book, complex_data):
        assert (list(book.books_genre.keys())[0] in
                book.get_books_with_specific_genre(list(book.books_genre.values())[0]))

    def test_get_books_with_specific_genre_not_shows_selected_genre(self, book, complex_data):
        assert (list(book.books_genre.keys())[0] not in book.get_books_with_specific_genre(book.genre[1]))

    def test_get_books_with_specific_genre_return_empty_list_with_incorrect_genre(self, book, complex_data):
        assert book.get_books_with_specific_genre(DATA.NON_EXISTING_GENRE) == []

    def test_get_books_with_specific_genre_try_non_existing_genre(self, book, complex_data):
        assert len(book.get_books_with_specific_genre(DATA.NON_EXISTING_GENRE)) == 0

    def test_get_books_genre_return_data(self, book, complex_data):
        assert len(book.get_books_genre()) != 0

    def test_get_books_for_children_return_safe_result(self, book, complex_data):
        for key, value in book.books_genre.items():
            if value in book.genre_age_rating:
                assert key not in book.get_books_for_children()
            else:
                assert key in book.get_books_for_children()

    def test_add_book_in_favorites_adds_existing_book(self, book, complex_data):
        book.add_book_in_favorites(DATA.BOOK_LIST[2])
        assert DATA.BOOK_LIST[2] in book.favorites

    def test_add_book_in_favorites_dont_add_non_existing_book(self, book, complex_data):
        book.add_book_in_favorites(DATA.NON_EXISTING_BOOK)
        assert DATA.NON_EXISTING_BOOK not in book.favorites

    def test_add_book_in_favorites_dont_add_duplicate(self, book, complex_data):
        for textbook in range(2):
            book.add_book_in_favorites(DATA.BOOK_LIST[0])
        assert book.favorites.count(DATA.BOOK_LIST[0]) == 1

    def test_delete_book_from_favorites_deletes_chosen_name(self, book, complex_data):
        book.add_book_in_favorites(DATA.BOOK_LIST[0])
        book.delete_book_from_favorites(DATA.BOOK_LIST[0])
        assert book.favorites.count(DATA.BOOK_LIST[0]) == 0

    def test_delete_book_from_favorites_try_delete_non_added_book(self, book, complex_data):
        book.delete_book_from_favorites(DATA.BOOK_LIST[0])
        assert book.favorites.count(DATA.BOOK_LIST[0]) == 0

    def test_get_list_of_favorites_books_return_created_list(self, book, complex_data):
        for textbook in DATA.BOOK_LIST:
            book.add_book_in_favorites(textbook)
        assert len(book.get_list_of_favorites_books()) == len(DATA.BOOK_LIST)
