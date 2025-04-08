class Library:

    def __init__(self, name):
        self.name = name
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print(f'Book {book.title} added.')

    def remove_book(self, isbn):
        for book in self.book_list:
            if book.isbn == isbn:
                self.book_list.remove(book)
                print(f'Book {book.title} removed.')
            else:
                print("No book with this isbn.")


    def book_list(self):
        print("Book lis of library", self.name)
        for book in self.book_list:
            print(f'Title: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}')

    def get_book_by_title(self, book, title):
        for book in self.book_list:
            if book.title == title:
                print(f'Title: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}')
                return book
            else:
                print("Book not found")



