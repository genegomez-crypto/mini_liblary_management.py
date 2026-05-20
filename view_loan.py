class Book:
    def __init__(self, title):
        self.title = title

class Member:
    def __init__(self, name):
        self.name = name

class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True

class LibraryService:
    def __init__(self):
        self._loans = []

    def view_loans(self):
        return list(self._loans)

def view_loans(service):
    loans = service.view_loans()
    
    if not loans:
        print("No loans found.")
    else:
        print("Loans:")
        for loan in loans:
            if loan.is_active is True:
                status = "Active"
            else:
                status = "Closed"
            print(f"{loan.loan_id} - {loan.member.name} borrowed {loan.book.title} [{status}]")

def main():
    service = LibraryService()
    
    while True:
        print("\n7. View Loans")
        print("0. Exit")
        choice = input("Enter choice: ")
        
        if choice == "7":
            view_loans(service)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
