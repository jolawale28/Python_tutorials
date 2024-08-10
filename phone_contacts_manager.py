def main():

    contactList = [("Alice", "123-456-7890"), ("Bob", "987-654-3210")]

    while (True):

        print("Options")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")

        userChoice = input("Enter your choice: ")

        if (userChoice == '1'):
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")

            contactTuple = (name, phone)
            contactList.append(contactTuple)

        elif (userChoice == '2'):
            searchName = input("Enter contact name to search: ")
            isFound = False
            contactFound = ()
            for contact in contactList:
                if (searchName.lower() in contact[0].lower()):
                    isFound = True
                    contactFound = contact
            if (isFound):
                print(f"Phone number for {searchName}: {contactFound[1]}\n")
            else:
                print(f"No contact found for: {searchName}\n")

        elif (userChoice == "3"):
            for contact in contactList:
                print(f"Name: {contact[0]}, Phone: {contact[1]}")
            print("\n")

        elif (userChoice == '4'):
            break
        
        else:
            print("Sorry, your input was not recognised!")
            break

if __name__ == "__main__":
    main()