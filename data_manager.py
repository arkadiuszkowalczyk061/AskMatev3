ANSWERS_PATH = 'sample_data/answer.csv'
QUESTIONS_PATH = 'sample_data/question.csv'
import csv
from csv import writer

def import_questions():
    questions = []
    csv_file = open(QUESTIONS_PATH, 'r')
    lines = csv.reader(csv_file)
    for row in lines:
        questions.append(row)
    return questions


def import_answers():
    answers = []
    csv_file = open(ANSWERS_PATH, 'r')
    lines = csv.reader(csv_file)
    for row in lines:
        answers.append(row)
    return answers


def append_data(file_name, list_of_elements):
    with open(file_name, 'a+') as write_obj:
        writer=csv.writer(write_obj)
        writer.writerow(list_of_elements)

def new_question(QUESTIONS_PATH, new_line):
    with open(QUESTIONS_PATH, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(new_line)