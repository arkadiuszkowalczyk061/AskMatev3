from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager, random, psycopg2, psycopg2.extras

# COL_TITLES = ['Title', 'Description']
# questions = [{'Id': 0, 'Title': 'Tisstleasfd', 'Description': 'Descriafsdpafdtion'}]

QUESTIONS = data_manager.import_questions()
ANSWERS = data_manager.import_answers()

TITLES_QUESTIONS = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
TITLES_ANSWERS = ['ID', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS, titles=TITLES_QUESTIONS)

@app.route('/add_answer/<id>', methods=['POST'])
def add_answer(id):
    new_record = dict(request.form)
    new_record_data = list(new_record.values())[0]
    # new_record_data = next(iter(new_record.values()))
    new_answer = ['ID', 'subtime', 'vote', new_record_data, 'message']
    data_manager.append_data('sample_data/answer.csv', new_answer)
    return redirect(url_for('index'))




@app.route('/add_question', methods=['POST', "GET"])
def add_question():
    global questions
    if request.method == 'POST':
        new_question = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
        new_question[0] = int(QUESTIONS[-1][0]) + 1
        new_question[1] = 150
        new_question[2] = 10
        new_question[3] = 15
        new_question[4] = request.form['Title']
        new_question[5] = request.form['Message']
        new_question[6] = ' '

        QUESTIONS.append(new_question)
        data_manager.new_question('sample_data/question.csv', new_question)
        return redirect(url_for('index'))
    else:
        return render_template('add_question.html')


@app.route('/display_question/<id>', methods=['POST', "GET"])
def display_question(id):
    id = int(id)
    question_data = QUESTIONS[id - 1]
    title = question_data[4]
    message = question_data[5]
    return render_template('display_question.html', questions=QUESTIONS, title=title, message=message, id=id)



if __name__ == '__main__':
    app.run()
