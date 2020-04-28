# ANSWERS_PATH = 'sample_data/answer.csv'
# QUESTIONS_PATH = 'sample_data/question.csv'
# import csv
# from csv import writer
import connection

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

get_all_questions()

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
    return table_headers
