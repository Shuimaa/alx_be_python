# oop/main.py

from book_class import Book

def main():
    # إنشاء كائن من Book
    my_book = Book("1984", "George Orwell", 1949)

    # تجربة __str__
    print(my_book)

    # تجربة __repr__
    print(repr(my_book))

    # تجربة __del__
    del my_book

if __name__ == "__main__":
    main()
