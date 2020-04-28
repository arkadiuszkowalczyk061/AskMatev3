from datetime import datetime
from connection import connection_handler, connection_handler_list

# ANSWERS_PATH = 'sample_data/answer.csv'
# QUESTIONS_PATH = 'sample_data/question.csv'
# import csv
# from csv import writer
#
# def import_questions():
#     questions = []
#     csv_file = open(QUESTIONS_PATH, 'r')
#     lines = csv.reader(csv_file)
#     for row in lines:
#         questions.append(row)
#     return questions
#
#
# def import_answers():
#     answers = []
#     csv_file = open(ANSWERS_PATH, 'r')
#     lines = csv.reader(csv_file)
#     for row in lines:
#         answers.append(row)
#     return answers
#
#
# def append_data(file_name, list_of_elements):
#     with open(file_name, 'a+') as write_obj:
#         writer=csv.writer(write_obj)
#         writer.writerow(list_of_elements)
#
# def new_question(QUESTIONS_PATH, new_line):
#     with open(QUESTIONS_PATH, 'a+', newline='') as write_obj:
#         csv_writer = writer(write_obj)
#         csv_writer.writerow(new_line)


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
    cursor.execute("""INSERT INTO questions VALUE (%(id)s, %(submission_time)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s);""",
                   {
                    'id': data_to_add['id'],
                    'submission_time': data_to_add['submission_time'],
                    'view_number': data_to_add['view_number'],
                    'vote_number': data_to_add['title'],
                    'message': data_to_add['message'],
                    'image': data_to_add['image']
                   })