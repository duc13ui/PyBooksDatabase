from utils2 import database2

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database2.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    #Asks the database to save the book
    database2.add_book(name, author)

def list_books():
    #Asks the database to get all of the books
    books = database2.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO' # If true, Yes. If false, No
        print(f"{book['name']} by {book['author']}, read: {read}")

def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database2.mark_book_as_read(name)

def prompt_delete_book():
    name = input('Enter the name of the book you would like to delete: ')

    database2.delete_book(name)


menu()