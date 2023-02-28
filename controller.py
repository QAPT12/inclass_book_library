from sql_functions import *
from prettytable import PrettyTable


def display_books():
    books = retrieve_all_books()
    col_names = list(books[0])
    data = []
    for book in books[1]:
        data.append(book)
    table = PrettyTable()
    table.field_names = col_names
    table.add_rows(data)
    table.align = 'l'
    return table


def add_book(title, author, pub_year):
    return insert_book(title, author, pub_year)


def edit_book(id, title, author, pub_year):
    return edit_book_by_id(id, title, author, pub_year)


def delete_book(id):
    return delete_book_using_id(id)

def search_book(keyword):
    pass


