from controller import *
from sql_functions import *


def menu_options():
    print('1. Display Books')
    print('2. Add Book')
    print('3. Edit Book')
    print('4. Delete Book')
    print('0. Exit')


if __name__ == '__main__':
    while True:
        menu_options()
        user_choice = input('Enter choice: ')

        match user_choice:
            case '0':
                break

            case '1':  # display books
                print(display_books())

            case '2':  # add new book
                try:
                    book_title = input('Title: ').strip()
                    author = input('Author: ').strip()
                    pub_year = int(input('Publication Year: '))
                    result = add_book(book_title, author, pub_year)
                except Exception as e:
                    print(f'error occurred: {e}')
                else:
                    if result == 1:
                        print('Book added successfully')

            case '3':  # edit book
                print(display_books())
                try:
                    book_to_edit = int(input('Enter the id of the book you wish to edit: '))
                    new_title = input('Title: ').strip()
                    new_author = input('Author: ').strip()
                    new_pub_year = int(input('Publication Year: '))
                    result = edit_book(book_to_edit, new_title, new_author, new_pub_year)
                    if result == 1:
                        print('Edit successful')

                except Exception as e:
                    print(f'error: {e}')

            case '4':  # delete book
                print(display_books())
                try:
                    book_to_delete = int(input('Enter the id of the book you wish to delete: '))
                    result = delete_book(book_to_delete)
                except Exception as e:
                    print(f'error: {e}')
            case '5':  # search function
                keyword = input('Enter search term (word in title or part of author name): ').strip()

            case _:
                print('Invalid option please try again')
