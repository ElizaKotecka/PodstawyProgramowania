class E_book:
    def __init__(self, title, author, num_of_pages, current_page):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.current_page = current_page
        self.is_open = False


    def open(self):
        if self.is_open:
            print('Book is already open!')
        else:
            self.is_open = True
            print('Opening your book.')

    def close(self):
        if self.is_open:
            self.is_open = False
            print('Closing your book.')
        else:
            print('Book is already closed!')
        
    def next_page(self):
        if self.is_open and self.current_page in range(0, self.num_of_pages):
            self.current_page += 1
            print("Swapping to next page...")
        elif not self.is_open:
            print("You can't read a book when it's closed!")
        else:
            print('There is no more pages. Congratulations!')
        
    def previous_page(self):
        if self.is_open and self.current_page in range(1, self.num_of_pages+1):
            self.current_page -= 1
            print("Swapping to previous page...")
        elif not self.is_open:
            print("You can't read a book when it's closed!")
        else:
            print("You have reached the beginning of the book.")
        
    def show_status(self):
        if self.is_open:
            print(f"Your book '{self.title}' by {self.author} is open. Book has {self.num_of_pages} pages, you are on page {self.current_page}.")
        else:
            print('Your book is closed.')