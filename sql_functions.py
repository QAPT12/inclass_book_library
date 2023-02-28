import mysql.connector


def execute_query_return_reult(query, host='localhost', username='root', password='root', port=3306,
                               database='library'):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.column_names, cursor.fetchall()


def execute_query_commit(query, host='localhost', username='root', password='root', port=3306, database='library'):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount


def insert_book(title, author, pub_year):
    sql = f"INSERT INTO books VALUES (default, '{title}', '{author}', '{pub_year}');"
    return execute_query_commit(sql)


def get_book_by_id(id):
    sql = f'SELECT * FROM books WHERE ID = {id};'
    return execute_query_return_reult(sql)


def delete_book_using_id(id):
    sql = f'DELETE FROM books WHERE ID = {id};'
    return execute_query_commit(sql)


def edit_book_by_id(id, title, author, pub_year):
    sql = f"UPDATE books SET Title = '{title}', Author = '{author}', Publication_Year = '{pub_year}' WHERE ID = '{id}';"
    return execute_query_commit(sql)

def retrieve_all_books():
    sql = 'SELECT * FROM books;'
    return execute_query_return_reult(sql)


def search_query_with_keyword(keyword):
    sql = f"SELECT * FROM books WHERE Title LIKE '%{keyword}%' or Author LIKE '%{keyword}%'"
    return execute_query_return_reult(sql)
