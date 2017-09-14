from flask import Flask, render_template, request, redirect
import queries
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_limited_list():
    data = queries.question_limited()
    return render_template('list.html', data=data)


@app.route('/show_all_questions', methods=['GET'])
def show_list():
    data = queries.question()
    return render_template('list.html', data=data)


@app.route("/new_question", methods=["GET"])
def new_question_form():
    users = queries.list_users()
    return render_template('new_question.html', users=users)


@app.route('/save_question', methods=['POST'])
def route_save():
    queries.add_new_question(request.form['title'], request.form['message'], request.form['pick_user'])
    return redirect('/')


@app.route('/save_registration', methods=['POST'])
def route_save_registration():
    queries.register_user(request.form['new_name'])
    return redirect('/')


@app.route('/list_users')
def list_users():
    users = queries.list_users()
    return render_template('all_users.html', users=users)


@app.route("/question/<id>", methods=["GET"])
def show_question(id):
    question = queries.show_question(id)
    answers = queries.show_answers(id)
    comments = queries.show_question_comment(id)
    users = queries.list_users()
    return render_template('question.html', id=id, question=question, answers=answers, comments=comments, users=users)


@app.route("/question/<id>/new_answer", methods=["POST"])
def new_answer(id):
    queries.add_new_answer(id, request.form['message'], request.form['pick_user'])
    return redirect("/question/"+str(id))


@app.route("/question/<id>/new_question_comment", methods=["POST"])
def new_question_comment(id):
    queries.add_new_question_comment(id, request.form['message'])
    return redirect("/question/"+str(id))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
