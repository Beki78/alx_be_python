class Book:
    def __init__ (self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

class Library:
    def __init__(self):
        self._books = []
    def add_book(self):
        self.addbook = True
    def check_out_book(self, title):
        self.title = title
    def return_book(self, title):
        self.title = title
    def list_available_books(self, available):
        self.available = available
        
        



