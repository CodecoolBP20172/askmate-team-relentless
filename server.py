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
    new_question = actions.create_question_list()
    csv_handling.append_question(new_question)
    return redirect('/')


@app.route("/question/<id>", methods=["GET"])
def show_question(id):
    question = actions.find_question(id)
    answer = actions.find_answer(id)
    return render_template('question.html', id=id, question=question, answer=answer)


@app.route("/questions/<id>/new_answer", methods=["POST"])
def new_answer(id):
    data = csv_handling.read_answers('answer.csv')
    new_answer = actions.create_answer_list(id)
    csv_handling.append_answer(new_answer)
    return redirect("/question/"+str(id))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
