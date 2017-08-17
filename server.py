from flask import Flask, render_template, request, redirect
import csv_handling
import actions

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_list():
    data = csv_handling.read_questions('question.csv')
    return render_template('list.html', data=data)


@app.route("/new_question", methods=["GET"])
def new_question_form():
    return render_template('new_question.html')


@app.route('/save_question', methods=['POST'])
def route_save():
    data = csv_handling.read_questions('question.csv')
    print('Question request received!')
    question = ['', '', '', '', '', '', '']
    question[0] = actions.new_id('question.csv')
    question[1] = actions.unixtime()
    question[4] = request.form['title']
    question[5] = request.form['message']
    csv_handling.append_question(question)
    return redirect('/')
    # get-render nq.html
    # post-új id, kiszedni a request.form-ból az adatokat és redirectelünk oda
    # return show_list


@app.route("/question/<id>", methods=["GET"])
def show_question(id):
    data = csv_handling.read_questions('question.csv')
    for row in data:
        if row[0] == id:
            question = row
    return render_template('question.html', question=question, id=id)

"""
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
