class Member:
    
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

class LibraryService:
   
    def __init__(self):
        self._members = {}

    def register_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        
        self._members[member.member_id] = member


def register_member(library_service):
    
    member_id = input("Enter Member ID: ")
    
   
    name = input("Enter Member Name: ")
    

    email = input("Enter Member Email: ")
    
   
    library_service.register_member(member_id, name, email)
    
   
    print(f"Member registered: {name}")


def main():
  
    library_service = LibraryService()
    
    while True:
      
        print("\n--- Library Menu ---")
        print("2. Register Member")
        print("0. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "2":
            register_member(library_service)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
