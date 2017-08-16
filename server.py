from flask import Flask, render_template, request, redirect
import csv_handling
import actions

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_list():
    data = csv_handling.read_questions('question.csv')
    return render_template('list.html', data=data)


@app.route("/new_question", methods=["GET", "POST"])
def new_question_form():
    return render_template('new_question.html', title=title, message=message)


@app.route('/save_question', methods=['POST'])
def route_save():
    print('Question request received!')
    print(request.form['title'])
    print(request.form['message'])
    print(question)
    csv_handling.append_question(question)
    return redirect('/')
    # get-render nq.html
    # post-új id, kiszedni a request.form-ból az adatokat és redirectelünk oda
    # return show_list

"""
@app.route("/question/<id>", methods=["GET"])
def show_question():
    # megjeleníti a questiont kiírja a válaszokat
    # a form actionje a new_answer
    # ha POST a request method, akkor return new_answer, máskülönben render template question.html
    # show answers.csv


@app.route("/questions/<id>/new_answer", method=["POST"])
def new_answer():
    # append answer.csv with new answer
    # redirect to question id

"""

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
