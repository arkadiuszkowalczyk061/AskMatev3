from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager, random, psycopg2, psycopg2.extras

# COL_TITLES = ['Title', 'Description']
# questions = [{'Id': 0, 'Title': 'Tisstleasfd', 'Description': 'Descriafsdpafdtion'}]

QUESTIONS = data_manager.get_all_questions()
ANSWERS = data_manager.get_all_answers()

TITLES_QUESTIONS = ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']
TITLES_ANSWERS = ['ID', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

app = Flask(__name__)


@app.route('/')
def index():
    questions = data_manager.get_all_questions()
    return render_template('index.html', questions=questions, titles=TITLES_QUESTIONS)


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
    global QUESTIONS
    if request.method == 'POST':
        new_question = {'id': QUESTIONS[-1].get('id') + 1,
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
