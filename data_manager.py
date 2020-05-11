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
        """INSERT INTO questions VALUES (%(id)s, %(submission_time)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s);""",
        {'id': data_to_add['id'],
         'submission_time': data_to_add['submission_time'],
         'view_number': data_to_add['view_number'],
         'vote_number': data_to_add['vote_number'],
         'title': data_to_add['title'],
         'message': data_to_add['message'],
         'image': data_to_add['image']})


@connection_handler
def write_data_to_answers(cursor, data_to_add):
    cursor.execute(
        """INSERT INTO answers VALUES (%(id)s, %(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s);""",
        {'id': data_to_add['id'],
         'submission_time': data_to_add['submission_time'],
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
        "id": get_next_answer_id(),
        "submission_time": datetime.now().replace(microsecond=0),
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
        'id': get_next_question_id(),
        'submission_time': datetime.now().replace(microsecond=0),
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
def get_question_by_id(cursor, question_id):
    cursor.execute("""SELECT * FROM questions
                    WHERE id=%(id)s;""",
                   {'id': question_id})
    question_data = cursor.fetchall()[0]
    return question_data

@connection_handler
def update_question_by_id(cursor, message, title,  question_id):
    cursor.execute("""
                    UPDATE questions
                    SET message = %(message)s, title = %(title)s
                    WHERE id=%(id)s""",
<<<<<<< HEAD
                   {'message': message, 'id': question_id})


@connection_handler
def get_all_questions_by_search(cursor, data_search):
    query = """
            SELECT *
            FROM questions
            WHERE upper(title) LIKE %(data_search)s OR upper(message) LIKE %(data_search)s OR lower(title) LIKE %(data_search)s OR lower(message) LIKE %(data_search)s """

    cursor.execute(query, {'data_search': "%" + data_search + "%"})
    return cursor.fetchall()
=======
                   {'message': message, 'title': title, 'id': question_id})
>>>>>>> bcaadd446dfb013ff9b0a9b43d937c1b3b7cb637
