from Book import Book
from Library import Library

library = Library("National library")

b_1 = Book("Basic Chemistry", "Walace Vangogue", 3454)
b_2 = Book("jiu-jitsu for beginners", "yuri nakamoto", 7194)
b_3 = Book("python from 0 to master", "aurelio zefra", 5578)

library.add_book(b_1)
library.add_book(b_2)
library.add_book(b_3)

print(library.book_list())
