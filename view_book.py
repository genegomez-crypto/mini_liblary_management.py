class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class LibraryService:
    def __init__(self):
        self._books = {}

    def view_books(self):
        return list(self._books.values())

def view_books(service):
    books = service.view_books()
    
    if not books:
        print("No books found.")
    else:
        print("Books:")
        for book in books:
            if book.available is True:
                status =
