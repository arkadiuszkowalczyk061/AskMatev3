from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager

# COL_TITLES = ['Title', 'Description']
# questions = [{'Id': 0, 'Title': 'Tisstleasfd', 'Description': 'Descriafsdpafdtion'}]

QUESTIONS=data_manager.import_questions()

TITLES= ['ID', 'Submission Time', 'View Number', 'Vote Number', 'Title', 'Message', 'Image']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS, titles=TITLES)

# @app.route('/add_answer/<id>')
# def add_answer(id):
#     pass



# @app.route('/add_question', methods=['POST', "GET"])
# def add_question():
#     global questions
#     if request.method == 'POST':
#         new_question = dict(request.form)
#         new_question['Title'] = request.form['Title']
#         new_question['Description'] = request.form['Description']
#
#         questions.append(new_question)
#         return redirect(url_for('display_question'))
#     else:
#         return render_template('add_question.html')


@app.route('/display_question/<id>', methods=['POST', "GET"])
def display_question(id):
    id = int(id)
    question_data = QUESTIONS[id - 1]
    title = question_data[4]
    message = question_data[5]
    return render_template('display_question.html', questions=QUESTIONS, title=title, message=message)



if __name__ == '__main__':
    app.run()
