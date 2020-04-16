from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    questions = data_manager.import_questions()
    return render_template('index.html', questions=questions)


@app.route('/add_question', methods=['POST', "GET"])
def add_question():
    global questions
    if request.method == 'POST':
        new_question = dict(request.form)
        new_question['Title'] = request.form['Title']
        new_question['Description'] = request.form['Description']

        questions.append(new_question)
        return redirect(url_for('display_question'))
    else:
        return render_template('add_question.html')


@app.route('/display_question', methods=['POST', "GET"])
def display_question():
    return render_template('display_question.html', questions=questions)



if __name__ == '__main__':
    app.run()
