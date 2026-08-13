class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self._isbn = isbn
        self.is_available = is_available

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return 'Success'
        else:
            return 'Unfortunately this books is not available at the moment!'

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return 'Success'
        else:
            return 'Error !'

    def get_details(self):
        if self.is_available:
            return f"{self.title} Book written by {self.author} is available."
        else:
            return f"{self.title} Book written by {self.author} is not available."

    def calculate_late_fee(self, days_late):
        return days_late* 1


class Ebook(Book):
    def __init__(self, title, author, isbn, file_size_mb, is_available = True):
        super().__init__(title, author, isbn, is_available)
        self.file_size_mb = file_size_mb

    def get_details(self):
        if self.is_available:
            return f"{self.title} E Book with file size {self.file_size_mb} and author {self.author} is available"
        else:
            return f"{self.title} E Book with file size {self.file_size_mb} and author {self.author} is not available"

    def calculate_late_fee(self,days_late):
        return days_late* 0.5

class AudioBook(Book):
    def __init__(self, title, author, isbn, duration_hours, is_available = True):
        super().__init__(title, author, isbn, is_available)
        self.duration_hours = duration_hours

    def get_details(self):
        if self.is_available:
            return f"{self.title} Audio Book with total duration {self.duration_hours} and author {self.author} is available"
        else:
            return f"{self.title} Audio Book with total duration {self.duration_hours} and author {self.author} is not available"

    def calculate_late_fee(self, days_left):
        return days_left* 0.75

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def list_all_books(self):
        for book in self._books:
            print(book.get_details())

    def find_by_title(self, title):
        search_title = title.strip().lower()
        for book in self._books:
            if book.title.strip().lower() == search_title:
                return book
        return None

    def checkout_book(self, title):
        book = self.find_by_title(title=title)
        if book:
            return book.checkout()

        return "Error!"

    def return_book(self, title):
        book = self.find_by_title(title=title)
        if book:
            return book.return_book()
        return "Error! Book not found in library."
    

    





    