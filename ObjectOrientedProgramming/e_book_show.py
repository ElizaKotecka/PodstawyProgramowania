from e_book import E_book

def main():
    book1 = E_book("The City of Bones", 'Cassandra Clare', 280, 34)
    book1.show_status()
    book1.open()
    book1.show_status()
    book1.next_page()
    book1.next_page()
    book1.next_page()
    book1.previous_page()
    book1.show_status()
    book1.close()
    book1.show_status()
    book1.next_page()

if __name__ == '__main__':
    main()

