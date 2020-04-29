from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager, random, psycopg2, psycopg2.extras

# COL_TITLES = ['Title', 'Description']
# questions = [{'Id': 0, 'Title': 'Tisstleasfd', 'Description': 'Descriafsdpafdtion'}]

QUESTIONS = data_manager.get_all_questions()
ANSWERS = data_manager.get_all_answers()

TITLES_QUESTIONS = ['ID', 'Title', 'Message']
TITLES_ANSWERS = ['ID', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

app = Flask(__name__)


@app.route('/')
def index():
    questions = data_manager.get_all_questions()
    return render_template('index.html', questions=questions, titles=TITLES_QUESTIONS)


@app.route('/add_answer/<id>', methods=['POST', 'GET'])
def add_answer(id):
    global ANSWERS, QUESTIONS
    id = int(id)
    if request.method == 'POST':
        new_answer = {'id': 0,
                     'submission_time': 0,
                     'vote_number': 0,
                     'question_id': QUESTIONS[id],
                     'message': request.form.get("Answer")}

        data_manager.write_data_to_answers(new_answer)
        return redirect(url_for('display_question.html'))


@app.route('/add_question', methods=['POST', "GET"])
def add_question():
    global QUESTIONS
    if request.method == 'POST':
        new_question = {'id': QUESTIONS[-1]('id') + 1,
                        'submission_time': 0,
                        'view_number': 0,
                        'vote_number': 0,
                        'title': request.form.get("Title"),
                        'message': request.form.get("Message"),
                        'image': '...'}

        data_manager.write_data_to_questions(new_question)
        return redirect(url_for('index'))
    else:
        return render_template('add_question.html')


@app.route('/display_question/<id>', methods=['POST', "GET"])
def display_question(id):
    id = int(id)
    question_data = QUESTIONS[id - 2]
    title = question_data['title']
    message = question_data['message']
    return render_template('display_question.html', questions=QUESTIONS, title=title, message=message, id=id)


if __name__ == '__main__':
    app.run()
