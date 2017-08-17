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


@app.route("/question/<id>", methods=["GET"])
def show_question(id):
    questions = csv_handling.read_questions('question.csv')
    answers = csv_handling.read_answers('answer.csv')
    for row in questions:
        if row[0] == id:
            question = row
    answer = []
    for row in answers:
        if row[3] == id:
            answer.append(row)
    return render_template('question.html', id=id, question=question, answer=answer)


@app.route("/questions/<id>/new_answer", methods=["POST"])
def new_answer(id):
    data = csv_handling.read_answers('answer.csv')
    print('Answer request received!')
    answer = ['', '', '', '', '', '']
    answer[0] = actions.new_id('answer.csv')
    answer[1] = actions.unixtime()
    answer[3] = id
    answer[4] = request.form['message']
    csv_handling.append_answer(answer)
    return redirect("/question/<id>")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
