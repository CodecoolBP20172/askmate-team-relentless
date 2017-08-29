import time
import datetime
import database_common


@database_common.connection_handler
def get_mentor_names(cursor):
    cursor.execute("SELECT CONCAT(first_name, ' ', last_name) as full_name FROM mentors ORDER BY first_name")
    names = cursor.fetchall()
    return names



"""
def base64_to_string(encoded_string):
    decoded_string = base64.b64decode(encoded_string)
    return decoded_string.decode('utf-8')


def string_to_base64(origin):
    origin_in_bytes = origin.encode('utf-8')
    b64_encoded_bytes = base64.b64encode(origin_in_bytes)
    return b64_encoded_bytes.decode('utf-8')


def new_id(csv_filename):
    with open(csv_filename, "r") as csv_file:
        lastrow = None
        for lastrow in csv.reader(csv_file):
            pass
        if lastrow is None:
            return 1
        else:
            return int(lastrow[0]) + 1


def unixtime():
    time_readable = datetime.datetime.fromtimestamp(
        int(int(time.time()))).strftime('%Y-%m-%d %H:%M:%S')
    return time_readable


def create_question_list():
    question = ['', '', '', '', '', '', '']
    question[0] = new_id('question.csv')
    question[1] = unixtime()
    question[4] = request.form['title']
    question[5] = request.form['message']
    return question


def create_answer_list(id):
    answer = ['', '', '', '', '', '']
    answer[0] = new_id('answer.csv')
    answer[1] = unixtime()
    answer[3] = id
    answer[4] = request.form['message']
    return answer


def find_question(id):
    questions = csv_handling.read_questions('question.csv')
    for question in questions:
        if question[0] == id:
            return question


def find_answer(id):
    answers = csv_handling.read_answers('answer.csv')
    answer = []
    for pick in answers:
        if pick[3] == id:
            answer.append(pick)
    return answer


"""
