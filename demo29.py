class Book:
    """Information about a book, including title, list of authors,
    publisher, ISBN, and prince.
    """

    def __init__(self, title, authors, publisher, isbn, price):
        """(Book, str, list of str, str, str, number) -> NoneType

        Create a new book entitled title, written by the people in authors,
        published by publisher, with ISBN isbn and costing prince dollars.

        >>> python_book = Book(
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-93778-545-1', \
                25.0)
        >>> python_book.title
        'Practical Programming'
        >>> python_book.authors
        ['Camobell', 'Gries', 'Montojo']
        >>> python_book.publisher
        'Pragmatic Bookshelf'
        >>> python_book.ISBN
        '978-1-93778-545-1'
        >>> python_book.price
        25.0
        """

        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def num_authors(self):
        """(Book) -> int

        Return the number of authors of this book.

        >>> python_book = Book(
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-93778-545-1', \
                25.0)
        >>> python_book.num_authors()
        3
        """

        return len(self.authors)

if __name__ == '__main__':

    python_book = Book(
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-93778-545-1', \
                25.0)
    print python_book.num_authors()



        




     