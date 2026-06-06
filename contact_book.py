contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"{name} added successfully!")

def search_contact(name):
    if name in contacts:
        print(f"{name}'s number is: {contacts[name]}")
    else:
        print("Contact not found.")

def show_all_contacts():
    if len(contacts) == 0:
        print("No contacts saved yet")
    else:
        print("\n--- All Contacts---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print("------------------")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully!")
    else:
        print("Contact not found.")

def edit_contact(name):
    if name in contacts:
        new_number = input("Enter new phone number: ")
        contacts[name] = new_number
        print(f"{name}'s number updated successfully!")
    else:
        print("Contact not found.")

#Main Program
while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        show_all_contacts()
    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "5":
        name = input("Enter a name to update its number: ")
        edit_contact(name)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")