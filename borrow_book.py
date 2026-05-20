class BookNotFoundError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

class BookUnavailableError(Exception):
    pass

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True
        
    def borrow(self):
        self.available = False

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []

    def borrow_book(self, book_id, member_id):
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
            
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
            
        if book.available is False:
            raise BookUnavailableError("Book is already borrowed.")
            
        book.borrow()
        loan_id = f"L{len(self._loans) + 1:03}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return member, book

def borrow_book(library_service):
    book_id = input("Enter Book ID: ")
    member_id = input("Enter Member ID: ")
    
    try:
        member, book = library_service.borrow_book(book_id, member_id)
        print(f"{member.name} borrowed {book.title}")
    except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
        print(e)

def main():
    library_service = LibraryService()
    
    while True:
        print("\n3. Borrow Book")
        print("0. Exit")
        choice = input("Enter choice: ")
        
        if choice == "3":
            borrow_book(library_service)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
