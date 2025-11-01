# contact_book.py

# A simple Contact Book Application using a Python dictionary

def display_menu():
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {'phone': phone, 'email': email}
    print(f"\n✅ Contact '{name}' added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nFound Contact:\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}")
    else:
        print("\n❌ Contact not found.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print(f"Updating contact '{name}'...")
        phone = input("Enter new phone (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"\n✅ Contact '{name}' updated successfully!")
    else:
        print("\n❌ Contact not found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"\n🗑️ Contact '{name}' deleted successfully!")
    else:
        print("\n❌ Contact not found.")


def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
