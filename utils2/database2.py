"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name, author, read\n
name, author, read\n
name, author, read\n
"""

books_file = 'books.txt'

def create_book_table():
    with open('books_file', 'w'):
        pass # Makes sure the file is there

def add_book(name, author):
    with open('books_file', 'a') as file:
        file.write(f'{name},{author},0\n')
    #books_file.append({'name': name, 'author': author, 'read': False})

def get_all_books():
    #opens the file
    with open('books_file', 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()] # Read lines and put it in a list and strip white space

    return [ # [[name, author, read], [name, author, read]]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

def mark_book_as_read(name):
    books = get_all_books() # Read all the books
    # Modify the book we want
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books) # Saves them all back

# Opens file, delete all contents, goes through all of items in parameter, and types it in csv format
def _save_all_books(books):
    with open('books_file', 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

