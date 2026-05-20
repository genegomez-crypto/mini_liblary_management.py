class Book:
    """Represents a book in the library."""
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        # Flowchart specifies: with available = True
        self.available = True 

class LibraryService:
    """Handles the business logic for library operations."""
    def __init__(self):
        # Dictionary to store books as specified in the flowchart
        self._books = {}

    def add_book(self, book_id, title, author):
        # Step: Create Book(book_id, title, author) with available = True
        book = Book(book_id, title, author)
        
        # Step: Store book in _books dictionary key = book.book_id
        self._books[book.book_id] = book


def add_book(library_service):
    """Handles the user inputs and outputs for adding a book."""
    # Step: Input: Book ID
    book_id = input("Enter Book ID: ")
    
    # Step: Input: Book Title
    title = input("Enter Book Title: ")
    
    # Step: Input: Book Author
    author = input("Enter Book Author: ")
    
    # Call the service layer to process the data
    library_service.add_book(book_id, title, author)
    
    # Step: Output: "Book added: {title}"
    print(f"Book added: {title}")


def main():
    """Main entry point simulating main.py"""
    library_service = LibraryService()
    
    while True:
        # Step: Display menu and read user choice = "1"
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("0. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_book(library_service)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
