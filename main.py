class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites


book = BooksCollector()
book.add_new_book('Коррректное имя')
print(book.books_genre)
book.add_new_book('Фантастика')
print(book.books_genre)
book.add_new_book('Фантастика')
print(book.books_genre)
book.add_new_book('К9 Собачья работа')
print(book.books_genre)
book.add_new_book('40символов_тестовые_пробелы_____________')
print(book.books_genre)
book.add_new_book('41символ___тестовые_пробелы______________')
print(book.books_genre)
print('zjopa' in book.books_genre)
book.add_new_book('42символа___тестовые_пробелы______________')
print(book.books_genre)
book.add_new_book(' Пробел в начале')
print(book.books_genre)
book.add_new_book('                 ')
print(book.books_genre)
book.set_book_genre('К9 Собачья работа','Комедии')
print(book.books_genre)
book.set_book_genre('Фантастика','Ужасы')
book.set_book_genre('Фантастика','неУжасы')
print(book.books_genre)
book.set_book_genre('Фантастика','Комедии')
print(book.books_genre)
print(book.books_genre['Фантастика'] == 'Комедии')
book.set_book_genre('Фантастика','ГОВНО')
print(book.books_genre)
book.set_book_genre(' Пробел в начале','Ужасы')
book.set_book_genre('40символов_тестовые_пробелы_____________','Мультфильмы')
print(book.books_genre)
print(book.get_book_genre('Фантастика'))
print(book.get_book_genre('40символов_тестовые_пробелы_____________'))
print(book.books_genre['Фантастика'] == book.get_books_genre())
print(book.get_books_genre())
print('ZHOPA')
print(book.get_book_genre('Фантастика'))
print(book.books_genre['Фантастика'])

print(book.get_books_with_specific_genre('Комедии'))
print('Фантастика' and 'К9 Собачья работа' in book.get_books_with_specific_genre('Комедии'))
book.add_new_book('Интерстеллар')
book.set_book_genre('Интерстеллар', 'Легенда')
print()
print('______________________________________________')
print()
print(book.books_genre['К9 Собачья работа'])
for key, value in book.books_genre.items():
    print(key, 'и его жанр', value)

print(book.get_books_genre())
print(len(book.get_books_genre()))
for key, value in book.get_books_genre().items():
    if ' Пробел в начале' in key and value == 'Ужасы':
        pass
print(book.get_books_genre())
print(book.get_books_for_children())
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

print(book.get_books_for_children())
print(len(book.get_books_for_children()))


# for i in book.get_books_for_children():
#     print(i)
#     if i in book.books_genre:
#         print(book.books_genre[i])
#         if book.books_genre[i] == 'Ужасы' or book.books_genre[i] == 'Детективы':
#             print('КОСЯК')
#     print('____________________________________')

book.add_new_book('НЕ Детское кино - 5')
book.set_book_genre('НЕ Детское кино - 5', 'Детективы')
print(book.get_books_for_children())
print(len(book.get_books_for_children()))
print('НЕ Детское кино - 5' in book.get_books_for_children())

print(book.books_genre)
for key, value in book.books_genre.items():
    if value == 'Ужасы' or value == 'Детективы':
        print(key in book.get_books_for_children())
