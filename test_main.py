import DATA
from main import BooksCollector
import pytest


class TestBooksCollector:

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

    def test_set_book_genre_genre_not_update_with_incorrect_data(self, book, correct_pair):
        temp_first_genre = book.books_genre[DATA.CORRECT_NAMES[0]]
        book.set_book_genre(DATA.CORRECT_NAMES[0], "Некорректный Жанр")
        temp_second_genre = book.books_genre[DATA.CORRECT_NAMES[0]]
        assert temp_first_genre == temp_second_genre

    def test_get_book_genre_return_correct_genre(self, book, correct_pair):
        assert book.get_book_genre(DATA.CORRECT_NAMES[0]) == book.books_genre[DATA.CORRECT_NAMES[0]]

    def test_get_books_with_specific_genre_shows_selected_genre(self, book):
        book.add_new_book('К9 - Собачья работа')
        book.set_book_genre('К9 - Собачья работа', 'Комедии')
        book.add_new_book('Флаббер')
        book.set_book_genre('Флаббер', 'Комедии')
        book.add_new_book('Робокоп')
        book.set_book_genre('Робокоп', 'Фантастика')
        book.add_new_book('Интерстеллар')
        book.set_book_genre('Интерстеллар', 'Легенда')
        book.get_books_with_specific_genre('Легенда')

        assert (('Флаббер' and 'К9 - Собачья работа' in book.get_books_with_specific_genre('Комедии') and
                 len(book.get_books_with_specific_genre('Комедии')) == 2) and
                ('Робокоп' in book.get_books_with_specific_genre('Фантастика')) and
                len(book.get_books_with_specific_genre('Фантастика')) == 1)

    def test_get_books_genre_return_dict(self, book, correct_pair):
        for key, value in book.get_books_genre().items():
            assert key == DATA.CORRECT_NAMES[0] and value == book.genre[0]

    def test_get_books_for_children_return_safe_result(self, book, complex_data):
        for key, value in book.books_genre.items():
            if value == 'Ужасы' or value == 'Детективы':
                assert key not in book.get_books_for_children()
            else:
                assert key in book.get_books_for_children()

    def test_add_book_in_favorites_adds_books(self, book, complex_data):
        book.add_book_in_favorites('НЕ Детское кино - 3')
        book.add_book_in_favorites('Не добавленное кино')
        book.add_book_in_favorites('Детское кино - 1')
        book.add_book_in_favorites('Детское кино - 1')
        assert (len(book.favorites) == 2 and 'Не добавленное кино' not in book.favorites and 'НЕ Детское кино - 3' in
                book.favorites and 'Детское кино - 1' in book.favorites)

    def test_delete_book_from_favorites_deletes_chosen_name(self, book, complex_data):
        book.add_book_in_favorites('НЕ Детское кино - 3')
        book.add_book_in_favorites('Не добавленное кино')
        book.add_book_in_favorites('Детское кино - 1')
        book.add_book_in_favorites('Детское кино - 1')
        book.add_book_in_favorites('Детское кино - 3')
        book.delete_book_from_favorites('Детское кино - 1')
        book.delete_book_from_favorites('Детское кино - 1')
        assert (len(book.favorites) == 2 and 'Не добавленное кино' not in book.favorites and 'НЕ Детское кино - 3' in
                book.favorites and 'Детское кино - 3' in book.favorites and 'Детское кино - 1' not in book.favorites)

    def test_get_list_of_favorites_books_return_created_list(self,book,complex_data):
        book.add_book_in_favorites('НЕ Детское кино - 3')
        book.add_book_in_favorites('Не добавленное кино')
        book.add_book_in_favorites('Детское кино - 1')
        book.add_book_in_favorites('Детское кино - 1')
        book.add_book_in_favorites('Детское кино - 3')
        assert ((len(book.get_list_of_favorites_books()) == 3 and 'НЕ Детское кино - 3'
                in book.get_list_of_favorites_books()) and 'Детское кино - 1' in book.get_list_of_favorites_books() and
                'Детское кино - 3' in book.get_list_of_favorites_books())
