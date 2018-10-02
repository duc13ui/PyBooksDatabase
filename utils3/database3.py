from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database.

"""

books_file = 'books.json'

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        #Query to create our table
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # [(name, author, read), (name, author, read)]

    return books

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))

