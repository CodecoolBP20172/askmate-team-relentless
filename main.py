from flask import Flask, render_template, request, redirect
import queries #actions
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_list():
    #data = queri_dict#
    return render_template('list.html', data=data)


@app.route("/new_question", methods=["GET"])
def new_question_form():
    return render_template('new_question.html')


@app.route('/save_question', methods=['POST'])
def route_save():
    #sql insert input alapján 
    return redirect('/')


@app.route("/question/<id>", methods=["GET"])
def show_question(id):
    #sql queri alapján megmutatja a kérdést
    return render_template('question.html', id=id, question=question, answer=answer)


@app.route("/questions/<id>/new_answer", methods=["POST"])
def new_answer(id):
    #sql insert(válasz) input alapján a kiválasztott kérdéshez
    return redirect("/question/"+str(id))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
