def add_contact(contacts, name, phone):
    contacts.append((name, phone))

def search_contact(contacts, name):
    for contact in contacts:
        if contact[0] == name:
            return contact[1]
    return "Contact not found."

def display_contacts(contacts):
    for contact in contacts:
        print(f"{contact[0]}: {contact[1]}")

def main():
    contacts = [("Alice", "123-456-7890"), ("Bob", "987-654-3210")]
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            phone = search_contact(contacts, name)
            print(f"Phone number for {name}: {phone}")
        elif choice == '3':
            display_contacts(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
