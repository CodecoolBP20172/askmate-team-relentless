from flask import Flask, render_template, request, redirect
import queries
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_limited_list():
    data = queries.questionLimited()
    return render_template('list.html', data=data)


@app.route('/show_all_questions', methods=['GET'])
def show_list():
    data = queries.question()
    return render_template('list.html', data=data)


@app.route("/new_question", methods=["GET"])
def new_question_form():
    return render_template('new_question.html')


@app.route('/save_question', methods=['POST'])
def route_save():
    queries.addNewQuestion(request.form['title'], request.form['message'])
    return redirect('/')


@app.route("/question/<id>", methods=["GET"])
def show_question(id):
    question = queries.showQuestion(id)
    answers = queries.showAnswers(id)
    return render_template('question.html', id=id, question=question, answers=answers)


@app.route("/question/<id>/new_answer", methods=["POST"])
def new_answer(id):
    queries.addNewAnswer(id, request.form['message'])
    return redirect("/question/"+str(id))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
