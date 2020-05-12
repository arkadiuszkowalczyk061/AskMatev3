from connection import connection_handler, connection_handler_list
from datetime import datetime


@connection_handler
def get_all_answers(cursor):
    cursor.execute("""SELECT * FROM answers""")
    answers = cursor.fetchall()
    return answers


@connection_handler
def get_all_questions(cursor):
    cursor.execute("""SELECT * FROM questions""")
    questions = cursor.fetchall()
    return questions


@connection_handler
def get_all_comments(cursor):
    cursor.execute("""SELECT * FROM comments""")
    comments = cursor.fetchall()
    return comments


@connection_handler
def get_all_question_headers(cursor):
    cursor.execute("""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
                      WHERE TABLE_NAME = 'questions';""")
    table_headers = cursor.fetchall()
    return (table_headers)


@connection_handler
def get_all_answer_headers(cursor):
    cursor.execute("""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
                      WHERE TABLE_NAME = 'answers';""")
    table_headers = cursor.fetchall()
    return table_headers


@connection_handler
def write_data_to_questions(cursor, data_to_add):
    cursor.execute(
        """INSERT INTO questions (title, message, view_number, vote_number, image) VALUES (%(title)s, %(message)s, %(view_number)s, %(vote_number)s, %(image)s);""",
        {
         'title': data_to_add['title'],
         'message': data_to_add['message'],
         'view_number': data_to_add['view_number'],
         'vote_number': data_to_add['vote_number'],
         'image': data_to_add['image']})


@connection_handler
def write_data_to_answers(cursor, data_to_add):
    cursor.execute(
        """INSERT INTO answers (vote_number, question_id, message) VALUES (%(vote_number)s, %(question_id)s, %(message)s);""",
        {
         'vote_number': data_to_add['vote_number'],
         'question_id': data_to_add['question_id'],
         'message': data_to_add['message']})


@connection_handler
def get_next_answer_id(cursor):
    cursor.execute("""SELECT MAX(id) from answers;""")
    new_id = cursor.fetchall()[0]['max'] + 1
    return new_id


def add_new_answer(new_answer, question_id):
    new_answer_data = {
        "vote_number": 0,
        "question_id": question_id,
        "message": new_answer,
        "image": ""
    }
    write_data_to_answers(new_answer_data)


@connection_handler
def get_next_question_id(cursor):
    cursor.execute("""SELECT MAX(id) from questions;""")
    new_id = cursor.fetchall()[0]['max'] + 1
    return new_id


def add_new_question_data():
    new_question_data = {
        'view_number': 0,
        'vote_number': 0
    }
    return new_question_data


@connection_handler
def delete_question(cursor, id):
    cursor.execute("""
                DELETE FROM questions
                WHERE id = %(id)s;
                DELETE FROM answers
                WHERE question_id = %(id)s;
                """,
                   {'id': id})


@connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute("""
                DELETE FROM answers
                WHERE id=%(answer_id)s;
                """,
                   {'answer_id': answer_id})


@connection_handler
def delete_comment(cursor, comment_id):
    query = """
            DELETE FROM comments
            WHERE id=%(comment_id)s;"""

    cursor.execute(query, {'comment_id': comment_id})


@connection_handler
def get_question_by_id(cursor, question_id):
    cursor.execute("""SELECT * FROM questions
                    WHERE id=%(id)s;""",
                   {'id': question_id})
    question_data = cursor.fetchall()[0]
    return question_data


@connection_handler
def update_question_by_id(cursor, message, title, question_id):
    cursor.execute("""
                    UPDATE questions
                    SET message = %(message)s, title = %(title)s
                    WHERE id=%(id)s""",
                   {'message': message, 'id': question_id})


@connection_handler
def get_answer_by_id(cursor, answer_id):
    cursor.execute("""
                    SELECT message
                    from answers
                    WHERE id=%(answer_id)s""",
                   {'answer_id': answer_id})
    message = cursor.fetchall()[0]['message']
    return message


@connection_handler
def update_question_by_id(cursor, message, title, question_id):
    cursor.execute("""
                    UPDATE questions
                    SET message = %(message)s, title = %(title)s
                    WHERE id=%(id)s""", {'message': message, 'title': title, 'id': question_id})


@connection_handler
def get_all_questions_by_search(cursor, data_search):
    query = """
            SELECT *
            FROM questions
            WHERE upper(title) LIKE %(data_search)s OR upper(message) 
            LIKE %(data_search)s OR lower(title) LIKE %(data_search)s OR lower(message) LIKE %(data_search)s """

    cursor.execute(query, {'data_search': "%" + data_search + "%"})
    return cursor.fetchall()


@connection_handler
def get_next_user_login_id(cursor):
    cursor.execute("""SELECT MAX(id) from user_login;""")
    new_id = cursor.fetchall()[0]['max'] + 1
    return new_id


@connection_handler
def get_next_user_password_id(cursor):
    cursor.execute("""SELECT MAX(id) from user_password;""")
    new_id = cursor.fetchall()[0]['max'] + 1
    return new_id


@connection_handler
def write_new_user_login(cursor, login):
    query = ("""
        INSERT INTO user_login 
        VALUES (%(id)s, %(login)s);""")

    cursor.execute(query, {'id': get_next_user_login_id(), 'login': login})


@connection_handler
def write_new_user_password(cursor, password):
    query = ("""
        INSERT INTO user_password
        VALUES (%(id)s, %(password)s);""")

    cursor.execute(query, {'id': get_next_user_password_id(), 'password': password})


@connection_handler
def update_answer_by_id(cursor, message, answer_id):
    cursor.execute("""
                    UPDATE answers
                    SET message = %(message)s
                    WHERE id=%(id)s""",
                   {'message': message, 'id': answer_id})


@connection_handler
def write_new_comment(cursor, message, question_id, answer_id):
    query = ("""
            INSERT INTO comments (message, question_id, answer_id)
            VALUES (%(message)s, %(question_id)s, %(answer_id)s)""")

    cursor.execute(query, {'message': message, 'question_id': question_id, 'answer_id': answer_id})


@connection_handler
def get_last_5_questions(cursor):
    cursor.execute("""
                    SELECT *
                    FROM questions
                    ORDER BY submission_time desc  LIMIT 5""")
    return cursor.fetchall()

@connection_handler
def sort_last_questions(cursor, sorting_factor, order_direction='ASC'):
    cursor.execute(f"""
                    SELECT *
                    from questions
                    ORDER BY {sorting_factor} {order_direction} """)
    return cursor.fetchall()

