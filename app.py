from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager, random, psycopg2, psycopg2.extras


TITLES_QUESTIONS = ['ID', 'Title', 'Message']
TITLES_ANSWERS = ['ID', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

app = Flask(__name__)

@app.route('/')
def index():
    questions = data_manager.get_all_questions()
    return render_template('index.html', questions=questions, titles=TITLES_QUESTIONS)


@app.route('/add_answer/<id>', methods=['POST', 'GET'])
def add_answer(id):
    id = int(id)
    if request.method == 'POST':
        new_answer = request.form.get("Answer")

        data_manager.add_new_answer(new_answer, id)

        return redirect(url_for('display_question', id=id))


@app.route('/add_question', methods=['POST', "GET"])
def add_question():
    if request.method == 'POST':
        new_question_data = data_manager.add_new_question_data()
        new_question_data.update(
            {
                'title': request.form.get('Title'),
                'message': request.form.get('Message'),
                'image': ""
            }
        )
        data_manager.write_data_to_questions(new_question_data)
        return redirect(url_for('index'))
    else:
        return render_template('add_question.html')


@app.route('/display_question/<id>', methods=['POST', "GET"])
def display_question(id):
    answers=data_manager.get_all_answers()
    questions = data_manager.get_all_questions()
    id = int(id)
    question_data = data_manager.get_question_by_id(id)
    title = question_data['title']
    message = question_data['message']
    return render_template('display_question.html', questions=questions, title=title, message=message, id=id,
                           answers=answers)


@app.route('/question/<id>/', methods=['POST', 'GET'])
def delete_question(id):
    id = int(id)
    if request.method == 'POST':
        data_manager.delete_question(id)

        return redirect(url_for('index'))

    else:
        return render_template('delete_question_confirm.html', id = id)


if __name__ == '__main__':
    app.run()
