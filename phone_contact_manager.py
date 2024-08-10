def addContact(contactList, name, phone):
    contact = (name, phone)
    contactList.append(contact)

def displayContact(contactList):
    for contact in contactList:
        print(f"{contact[0]}: {contact[1]}")

def searchContact(contactList, name):
    contactFound = ()
    for contact in contactList:
        if (contact[0] == name):
            contactFound = contact
    return contactFound

def deleteContact(contactList, name):
    removed = False
    for contact, i in enumerate(contactList):
        if (contact[0] == name):
            removed = contactList.pop(i)
            return removed


def main():

    contactList = [("Vicky", "09045679873"), ("Ifeoma", "09067431267")] # Serving as contact database

    while True:
        print("Options: ")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            addContact(contactList, name, phone)

        elif (choice == '2'):
            name = input("Enter name of contact to search: ")
            contact = searchContact(contactList, name)

            if (contact):
                print(f"Phone number for {name}: {contact[1]}")
            else:
                print(f"No match found for: {name}")
        
        elif (choice == "3"):
            displayContact(contactList)

        elif (choice == "4"):
            name = input("Enter name of contact to delete: ")
            removedContact = deleteContact(contactList, name)
            if removedContact:
                print(f"Contact with name: {name} removed successfully.")
            else:
                print("Could not remove contact.")

        elif (choice == "6"):
            break
        else:
            print("The command you entered is not recognised!")

if __name__ == "__main__":
    main()