import time
from datetime import datetime
import database_common

my_format = '{0:%Y-%m-%d %H:%M:%S}'


@database_common.connection_handler
def question(cursor):
    cursor.execute("""SELECT *
                      FROM question
                      ORDER BY id DESC;""")
    rows = cursor.fetchall()
    return rows


@database_common.connection_handler
def questionLimited(cursor):
    cursor.execute("""SELECT *
                      FROM question
                      ORDER BY id DESC
                      LIMIT 5;""")
    rows = cursor.fetchall()
    return rows


@database_common.connection_handler
def showQuestion(cursor, id):
    cursor.execute("""SELECT *
                      FROM question
                      WHERE id=%s""", (id,))
    question = cursor.fetchall()
    return question


@database_common.connection_handler
def showAnswers(cursor, id):
    cursor.execute("""SELECT *
                      FROM answer
                      WHERE question_id=%s""", (id,))
    answers = cursor.fetchall()
    return answers


@database_common.connection_handler
#az insertbe itt még bele kell tenni a usert is (a legördülő menüből)
def addNewQuestion(cursor, title, message):
    cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message, image)
                      VALUES ((%s), 0, 0, (%s), (%s), '');""", (my_format.format(datetime.now()), title, message))


@database_common.connection_handler
def addNewAnswer(cursor, id, message):
    cursor.execute("""INSERT INTO answer (submission_time, vote_number, question_id, message, image)
                      VALUES ((%s), 0, (%s), (%s), '');""", (my_format.format(datetime.now()), id, message))


@database_common.connection_handler
def addNewQuestionComment(cursor, id, message):
    cursor.execute("""INSERT INTO comment (question_id, message, submission_time, edited_count)
                      VALUES ((%s), (%s),(%s), 0);""", (id, message, my_format.format(datetime.now())))


@database_common.connection_handler
def showQuestionComment(cursor, id):
    cursor.execute("""SELECT message
                      FROM comment
                      WHERE question_id=%s""", (id,))
    comments = cursor.fetchall()
    return comments


@database_common.connection_handler
def registerUser(cursor, new_name):
    cursor.execute("""INSERT INTO username(user_name, submission_time)
                      VALUES ((%s), (%s))
                      ON CONFLICT DO NOTHING;""", (new_name, my_format.format(datetime.now())))


@database_common.connection_handler
def listUsers(cursor):
    cursor.execute("""SELECT user_name, submission_time
                      FROM username
                      ORDER BY id DESC;""")
    users = cursor.fetchall()
    return users
