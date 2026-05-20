class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

class LibraryService:
    def __init__(self):
        self._members = {}

    def view_members(self):
        return list(self._members.values())

def view_members(service):
    members = service.view_members()
    
    if not members:
        print("No members found.")
    else:
        print("Members:")
        for member in members:
            print(f"{member.member_id} - {member.name} ({member.email})")

def main():
    service = LibraryService()
    
    while True:
        print("\n6. View Members")
        print("0. Exit")
        choice = input("Enter choice: ")
        
        if choice == "6":
            view_members(service)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
