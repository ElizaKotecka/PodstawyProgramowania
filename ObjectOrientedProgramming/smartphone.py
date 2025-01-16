from contact import Contact, ContactList

def main():
    contacts1 = ContactList()

    contacts1.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    contacts1.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    contacts1.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    contacts1.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    contacts1.display_contacts()


if __name__ == "__main__":
    main()