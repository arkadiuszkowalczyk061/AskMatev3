ANSWERS_PATH = 'sample_data/answer.csv'
QUESTIONS_PATH = 'sample_data/question.csv'
import csv

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
