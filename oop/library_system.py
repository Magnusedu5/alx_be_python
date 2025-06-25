class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}"

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"{super().get_details()},File_size: {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"{super().get_details()}, Pages: {self.page_count}"

class Library:
    def __init__(self, books):
        self.books = [Book, Ebook, PrintBook]

    def add_book(self, book):
        self.book = book
        self.books.append(book)

    def list_books(self):
        for book in  self.books:
            print(book.get_details())
