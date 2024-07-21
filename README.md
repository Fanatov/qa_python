# tests
* test_add_new_book_correct_input

Проверка на то, что корректное имя книги добавляется и отображается в словаре книг

* test_add_new_book_incorrect_input

Проверка на то, что некорректное имя книги не добавляется и не отображается в словаре книг

* test_set_book_genre_add_existing_genre

Проверяет добавление корректного жанра в словарь книг

* test_set_book_genre_add_non_existing_genre

Проверяет что некорректный жанр не добавляется в словарь книг

* test_set_book_genre_genre_not_update_with_incorrect_data

Проверка на то, что корректный жанр не заменяется некорректным

* test_get_book_genre_return_correct_genre

Проверка на то, что значение возвращаемое методом соответствует значению, находящемуся в словаре книг 

* test_get_books_with_specific_genre_shows_selected_genre

Проверка на то, что книга определенного жанра находится в результате вызова метода

* test_get_books_with_specific_genre_not_shows_selected_genre

Проверка на то, что книга определенного жанра отсутствует в результате вызова метода 

* test_get_books_with_specific_genre_return_empty_list_with_incorrect_genre

Проверка на то, что при передаче некорректного жанра возвращается пустой список

* test_get_books_with_specific_genre_try_non_existing_genre

Проверка получить все фильмы с несуществующим жанром

* test_get_books_genre_return_data

Проверка на то, что метод возвращает данные, а не пустое значение

* test_get_books_for_children_not_return_unsafe_result

Проверка на то, что если жанр книги не подходит детям, метод не возвращает книги этого жанра в списке разрешенных книг

* test_get_books_for_children_not_return_unsafe_result

Проверка на то, что если жанр книги подходит детям, метод возвращает книги этого жанра в списке разрешенных книг

* test_add_book_in_favorites_adds_existing_book

Проверка на то, что книга добавляемая методом содержится в списке избранного

* test_add_book_in_favorites_dont_add_non_existing_book

Проверка на то, что несуществующую книгу нельзя добавить в список избранного

* test_add_book_in_favorites_dont_add_duplicate

Проверка на то, что книга добавляется в избранное в единичном экземпляре

* test_delete_book_from_favorites_deletes_chosen_name

Проверка на то, что добавленная книга в список избранного удаляется

* test_delete_book_from_favorites_try_delete_non_added_book

Проверка на то, что при удалении не добавленной книги в список избранного ничего не происходит

* test_get_list_of_favorites_books_return_created_list

Проверка на то, что список избранного создается и содержит то количество записей, которое в него передавали