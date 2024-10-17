# main.py
from flask import Flask, render_template, request,redirect, url_for, redirect
import primary,middle,high

# app = Flask('app')
app = Flask(__name__, static_folder='static')
question_text='example'


@app.route('/')
def signUp():
    return render_template('welcome.html')

@app.route('/select_chapter', methods=['GET', 'POST'])
def select_chapter():
    return render_template('selectChapter.html',
                           welcome_url=url_for('welcome'))


@app.route('/signup')
def signup():
    return render_template('signUp.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/primary_school')
def primary_school():
    return render_template('question.html', level='Primary School Level')


@app.route('/middle_school')
def middle_school():
    return render_template('question.html', level='Middle School Level')


@app.route('/high_school')
def high_school():
    return render_template('question.html', level='High School Level')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/end')
def end():
    return render_template('end.html')


# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')  # Main homepage


# Route for example1.html
@app.route('/example1', methods=['GET', 'POST'])
def example1():
    result = None
    if request.method == 'POST': #and 'generate_question' in request.form:
        result = primary.question()  # Call the AI function

    return render_template('example1.html', question_text=result)


# Route for verifying the answer
@app.route('/verify_answer1', methods=['POST'])
def verify_answer1():
    user_answer = request.form['answer']  # Get user's answer from the form
    # Call the verify_answer function from primary.py
    verification_result = primary.verify_answer1(user_answer,question_text)

    return render_template('example1.html', user_answer=verification_result)


@app.route('/example2', methods=['GET', 'POST'])
def example2():
    result = None
    if request.method == 'POST':
        result = middle.question()  # Call the AI function

    return render_template('example2.html', question_text=result)

@app.route('/verify_answer2', methods=['POST'])
def verify_answer2():
    user_answer = request.form['answer']  # Get user's answer from the form
    # Call the verify_answer function from primary.py
    verification_result = middle.verify_answer2(user_answer,question_text)

    return render_template('example2.html', user_answer=verification_result)


@app.route('/example3', methods=['GET', 'POST'])
def example3():
    result = None
    if request.method == 'POST':
        result = high.question()  # Call the AI function

    return render_template('example3.html', question_text=result)

@app.route('/verify_answer3', methods=['POST'])
def verify_answer3():
    user_answer = request.form['answer']  # Get user's answer from the form
    # Call the verify_answer function from primary.py
    verification_result = high.verify_answer3(user_answer,question_text)

    return render_template('example3.html', user_answer=verification_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)