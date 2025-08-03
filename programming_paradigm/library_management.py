class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Initially the book is available

    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.check_out()
                return True
        print(f"Book '{title}' is not available for checkout.")
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.return_book()
                return True
        print(f"Book '{title}' is not found or already available.")
        return False


def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
