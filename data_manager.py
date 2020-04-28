from connection import connection_handler, connection_handler_list

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
    cursor.execute("""INSERT INTO questions VALUES (%(id)s, %(submission_time)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s);""",
                   {'id': data_to_add['id'],
                    'submission_time': data_to_add['submission_time'],
                    'view_number': data_to_add['view_number'],
                    'vote_number': data_to_add['vote_number'],
                    'title': data_to_add['title'],
                    'message': data_to_add['message'],
                    'image': data_to_add['image']})


@connection_handler
def write_data_to_answers(cursor, data_to_add):
    cursor.execute("""INSERT INTO answers VALUES (%(id)s, %(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s);""",
                {'id': data_to_add['id'],
                 'submission_time': data_to_add['submission_time'],
                 'vote_number': data_to_add['vote_number'],
                 'question_id': data_to_add['question_id'],
                 'message': data_to_add['message']})
