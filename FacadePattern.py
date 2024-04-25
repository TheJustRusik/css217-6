class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available


class BookInventorySystem:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def check_availability(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                return True
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                return True
        return False


class UserManagementSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        self.users[user_id] = name


class LibraryFacade:
    def __init__(self):
        self.book_inventory = BookInventorySystem()
        self.user_management = UserManagementSystem()

    def add_book(self, title, author):
        book = Book(title, author)
        self.book_inventory.add_book(book)

    def search_by_title(self, title):
        return self.book_inventory.search_by_title(title)

    def search_by_author(self, author):
        return self.book_inventory.search_by_author(author)

    def check_availability(self, title):
        return self.book_inventory.check_availability(title)

    def borrow_book(self, title):
        return self.book_inventory.borrow_book(title)

    def return_book(self, title):
        return self.book_inventory.return_book(title)


# Testing the facade
def test_library_facade():
    facade = LibraryFacade()

    # Adding books
    facade.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    facade.add_book("To Kill a Mockingbird", "Harper Lee")

    # Searching for books
    assert facade.search_by_title("The Great Gatsby")[0].author == "F. Scott Fitzgerald"
    assert facade.search_by_author("Harper Lee")[0].title == "To Kill a Mockingbird"

    # Checking availability
    assert facade.check_availability("The Great Gatsby") == True
    assert facade.check_availability("To Kill a Mockingbird") == True

    # Borrowing books
    assert facade.borrow_book("The Great Gatsby") == True
    assert facade.borrow_book("The Great Gatsby") == False  # Already borrowed
    assert facade.check_availability("The Great Gatsby") == False

    # Returning books
    assert facade.return_book("The Great Gatsby") == True
    assert facade.return_book("The Great Gatsby") == False  # Already returned
    assert facade.check_availability("The Great Gatsby") == True


if __name__ == "__main__":
    test_library_facade()
