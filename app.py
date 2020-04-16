from flask import Flask, request, redirect, url_for, abort, render_template
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    questions = data_manager.import_questions()
    return render_template('index.html', questions=questions)



if __name__ == '__main__':
    app.run()