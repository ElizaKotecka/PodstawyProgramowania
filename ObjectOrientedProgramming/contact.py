class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name:<15} {self.email:<20} {self.telephone}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("No contacts on the list.")
        else:
            print("Contact List:")
            print(f"Name            Email                Telephone")
            for contact in self.contacts:
                print(contact)