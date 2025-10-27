# 5. Library Management 
# o	Base class: LibraryItem (title, author)
# o	Derived classes: Book, Magazine
# o	Raise a BookNotAvailableError if user tries to borrow an unavailable book.
# o	Demonstrate try...except...finally to handle the borrowing process.


# -----------------------------
# 5. Library Management System
# -----------------------------

# Custom Exception
class BookNotAvailableError(Exception):
    """Raised when a book is not available to borrow."""
    pass


# Base Class
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Derived Class - Book
class Book(LibraryItem):
    def __init__(self, title, author, available=True):
        super().__init__(title, author)
        self.available = available

    def borrow(self):
        if not self.available:
            raise BookNotAvailableError(f"'{self.title}' is not available right now.")
        print(f"You have successfully borrowed '{self.title}' by {self.author}.")
        self.available = False


# Derived Class - Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)


# Demonstrating try...except...finally
print("=== Library Management System ===")
book1 = Book("Python Programming", "Guido van Rossum", available=True)
book2 = Book("Artificial Intelligence", "John McCarthy", available=False)

for book in [book1, book2]:
    try:
        book.borrow()
    except BookNotAvailableError as e:
        print("Error:", e)
    finally:
        print(f"Finished processing: {book.title}\n")
