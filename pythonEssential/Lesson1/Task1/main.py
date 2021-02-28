class MyBook:
    """
    Create list of objects (some different books) with parameters as: author, name, genre and year made.\n
    Fained oldest book.
    Used two methods of presentation:
        __repr__
        __str__
    """

    def __init__(self, a='Author', n='Name of the book', w=2021, g='Various genre'):
        self.author = a
        self.name_of_book = n
        self.was_made = w
        self.genre = g

    def __str__(self):
        book_info_s = f'Like  __str__ Book Author is: {self.author} \t Name of the book: {self.name_of_book} ' \
                    f'\t Year of made: {self.was_made} \t Genre: {self.genre}'
        return book_info_s

    def __repr__(self):
        book_info_r = f'Like __repr__ Book Author is: {self.author} \t Name of the book: {self.name_of_book} ' \
                      f'\t Year of made: {self.was_made} \t Genre: {self.genre}'
        return book_info_r

    def show(self):
        print(self.__str__())
        print(self.__repr__())
        return "-" * 150


b0 = MyBook()
b1 = MyBook('Vasya Pupkin', 'Someone', 1980, 'Pulp fiction')
b2 = MyBook('Taras Shevchenko', 'Kobzar', 1840, 'Poetry')
b3 = MyBook('Dan Brown', 'The Da Vinci Code', 2004, 'Detective')
b4 = MyBook('Did Opanas', 'Os taka *uinja maljata', 1984, 'Epic battle')

list_of_books = [b0, b1, b2, b3, b4]
min_year = list_of_books[0].was_made

for book in range(0, len(list_of_books)):
    print(list_of_books[book].show())

    if list_of_books[book].was_made < min_year:
        min_year = list_of_books[book].was_made


print(f"min year of made is:{min_year}")
