from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager, random, psycopg2, psycopg2.extras
import bcrypt
import os
from datetime import timedelta




TITLES_QUESTIONS = {'title': 'Title', 'message': 'Message', 'submission_time': 'Submission Time', 'view_number': '# of views', 'vote_number':'Votes'}
TITLES_ANSWERS = ['ID', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


app = Flask(__name__)
app.secret_key = (os.urandom(16))
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    data_search = request.args.get('search')
    if data_search:
        questions = data_manager.get_all_questions_by_search(data_search)
    else:
        questions = data_manager.get_last_5_questions()

    return render_template('index.html', questions=questions, titles=TITLES_QUESTIONS)

@app.route('/', methods=['POST'])
def sort_questions():
    order_by = request.form.get('order_by')
    order = request.form.get('order')
    questions = data_manager.sort_last_questions(order_by, order)

    return render_template('index.html', questions=questions, titles=TITLES_QUESTIONS)


@app.route('/list')
def list_questions():
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


@app.route('/add_comment/<question_id>/<answer_id>', methods=['POST', 'GET'])
def add_comment(question_id, answer_id):
    question_id = int(question_id)
    answer_id = int(answer_id)
    if request.method == 'POST':
        message = request.form.get('comment')
        data_manager.write_new_comment(message, question_id, answer_id)

        return redirect(url_for('display_question', id=question_id, answer_id=answer_id))


@app.route('/display_question/<id>', methods=['POST', "GET"])
def display_question(id):
    answers=data_manager.get_all_answers()
    questions = data_manager.get_all_questions()
    comments = data_manager.get_all_comments()
    id = int(id)
    question_data = data_manager.get_question_by_id(id)
    title = question_data['title']
    message = question_data['message']


    return render_template('display_question.html', questions=questions, title=title, message=message, id=id,
                           answers=answers, comments=comments)


@app.route('/display_question/<id>/edit', methods=['GET', 'POST'])
def edit_question(id):

    if request.method == 'GET':
        id = int(id)
        question_data = data_manager.get_question_by_id(id)
        title = question_data['title']
        message = question_data['message']

        return render_template('edit_question_answer.html', title=title, message=message, id=id)

    if request.method == 'POST':
        updated_title = request.form.get('updated_title')
        updated_message = request.form.get('updated_message')
        data_manager.update_question_by_id(updated_message, updated_title, id)

        return redirect(url_for('display_question', id=id))


@app.route('/display_question/<id>/<answer_id>/edit', methods=['POST', 'GET'])
def edit_answer(id, answer_id):

    if request.method == 'POST':
        updated_answer = request.form.get('updated_answer')
        data_manager.update_answer_by_id(updated_answer, id)

        return redirect(url_for('display_question', id=id))

    if request.method == 'GET':
        id = int(id)
        message = data_manager.get_answer_by_id(answer_id)

        return render_template('edit_question_answer.html', id=id, answer_id=answer_id, message=message)




@app.route('/question/<id>/', methods=['POST', 'GET'])
def delete_question(id):
    id = int(id)

    if request.method == 'POST':
        data_manager.delete_question(id)

        return redirect(url_for('index'))

    else:
        return render_template('delete_question_confirm.html', id=id)


@app.route("/display_question/<id>/<answer_id>/delete", methods=['POST'])
def delete_answer(id, answer_id):
    int(id)

    if request.method == 'POST':
        data_manager.delete_answer(answer_id)
        return redirect(url_for('display_question', id=id))

    else:
        return redirect('display_question.html')

@app.route("/display_question/<id>/<answer_id>/<comment_id>/delete", methods=['POST'])
def delete_comment(id, answer_id, comment_id):
    int(id)
    int(answer_id)

    if request.method == 'POST':
        data_manager.delete_comment(comment_id)
        return redirect(url_for('display_question', id=id, answer_id=answer_id))


@app.route('/register', methods=['POST', 'GET'])
def create_user():
    login = request.form.get('login')
    password = request.form.get('password')
    if request.method == 'POST':
        hash_pass = hash_password(password)
        print('password')
        data_manager.add_user_ta_database(login, hash_pass)
        return redirect(url_for('index'))

    else:
        return render_template('registration.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    auxiliary = 'yes'
    if request.method == 'POST':
        user = request.form.get('login')
        haslo = request.form.get('password')
        check = data_manager.search_user(user)
        result = [dict(row) for row in check]
        to_check = (result[0]['password'])
        if verify_password(haslo, to_check):
            print('mamy')

        return redirect(url_for('index'))
    return render_template('registration.html', login=auxiliary)




def hash_password(plain_password):
    hashed_bytes = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_bytes_password)





if __name__ == '__main__':
    app.run(debug= True)
