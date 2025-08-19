contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"\nFound Contact:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
            found = True
    if not found:
        print("❌ No contact found.\n")

def update_contact():
    keyword = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == keyword.lower():
            print("Enter new details (leave blank to keep current):")
            new_name = input(f"Name ({contact['name']}): ") or contact['name']
            new_phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"Email ({contact['email']}): ") or contact['email']
            new_address = input(f"Address ({contact['address']}): ") or contact['address']
            contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
            print("✅ Contact updated successfully!\n")
            return
    print("❌ Contact not found.\n")

def delete_contact():
    keyword = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == keyword.lower():
            contacts.remove(contact)
            print("✅ Contact deleted successfully!\n")
            return
    print("❌ Contact not found.\n")

def menu():
    while True:
        print("📞 Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

menu()
