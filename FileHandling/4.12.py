import csv

def read_books_from_csv(filename):
    books = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

def filter_books_by_genre(books, genre):
    filtered_books = []
    for book in books:
        if book['Genre'] == genre:
            filtered_books.append(book)
    return filtered_books

def write_books_to_file(filename, books):
    with open(filename, 'w') as file:
        for book in books:
            file.write(f"{book['Title']},{book['Author']},{book['Genre']},{book['Year']}\n")

# Function to process books by genre
def process_books_by_genre():
    books = read_books_from_csv('books.csv')
    
    genre_to_filename = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }
    
    # Process each genre and write filtered books to corresponding files
    for genre, filename in genre_to_filename.items():
        filtered_books = filter_books_by_genre(books, genre)
        write_books_to_file(filename, filtered_books)
        print(f"Books in the '{genre}' genre have been written to {filename}")

if __name__ == "__main__":
    process_books_by_genre()