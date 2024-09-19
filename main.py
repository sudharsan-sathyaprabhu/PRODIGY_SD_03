import json

# Function to load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new name: ")
        contacts[index]['phone'] = input("Enter new phone number: ")
        contacts[index]['email'] = input("Enter new email address: ")
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main function
def main():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
