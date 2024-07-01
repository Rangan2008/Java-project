class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name}: {contact.phone_number}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        return results

    def update_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                return True
        return False

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return True
        return False

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            print("\nContacts:")
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ").strip()
            results = contact_book.search_contact(keyword)
            if results:
                print("\nSearch Results:")
                for i, contact in enumerate(results, start=1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name of contact to update: ").strip()
            results = contact_book.search_contact(name)
            if results:
                new_phone_number = input("Enter new phone number: ").strip()
                new_email = input("Enter new email: ").strip()
                new_address = input("Enter new address: ").strip()
                updated_contact = Contact(name, new_phone_number, new_email, new_address)
                if contact_book.update_contact(name, updated_contact):
                    print("Contact updated successfully.")
                else:
                    print("Error updating contact.")
            else:
                print("Contact not found.")

        elif choice == '5':
            name = input("Enter name of contact to delete: ").strip()
            if contact_book.delete_contact(name):
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
