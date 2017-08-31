import time
from datetime import datetime
import database_common

dt = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())


@database_common.connection_handler
def question(cursor):
    cursor.execute("""SELECT *
                      FROM question
                      ORDER BY submission_time DESC;""")
    rows = cursor.fetchall()
    return rows


@database_common.connection_handler
def questionLimited(cursor):
    cursor.execute("""SELECT *
                      FROM question
                      ORDER BY submission_time DESC
                      LIMIT 5;""")
    rows = cursor.fetchall()
    return rows


@database_common.connection_handler
def showQuestion(cursor, id):
    cursor.execute("""SELECT *
                      FROM question
                      WHERE id={};""".format(id))
    question = cursor.fetchall()
    return question


@database_common.connection_handler
def showAnswers(cursor, id):
    cursor.execute("""SELECT *
                      FROM answer
                      WHERE question_id={};""".format(id))
    answers = cursor.fetchall()
    return answers


# @database_common.connection_handler NINCS RÁ SZÜKSÉÉÉÉG
# def showAnswer(cursor, id):
#     cursor.execute("""SELECT *
#                       FROM answer
#                       WHERE answer_id={};""".format(id))
#     answer = cursor.fetchall()
#     return answer


@database_common.connection_handler
def addNewQuestion(cursor, title, message):
    cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message, image)
                      VALUES ((%s), 0, 0, (%s), (%s), '');""", (dt, title, message))


@database_common.connection_handler
def addNewAnswer(cursor, id, message):
    cursor.execute("""INSERT INTO answer (submission_time, vote_number, question_id, message, image)
                      VALUES ((%s), 0, (%s), (%s), '');""", (dt, id, message))


@database_common.connection_handler
def addNewQuestionComment(cursor, id, message):
    cursor.execute("""INSERT INTO comment (question_id, message, submission_time, edited_count)
                      VALUES ((%s), (%s),(%s), 0);""", (id, message, dt))


@database_common.connection_handler
def showQuestionComment(cursor, id):
    cursor.execute("""SELECT message
                      FROM comment
                      WHERE question_id={};""".format(id))
    questioncomments = cursor.fetchall()
    return questioncomments


@database_common.connection_handler
def addNewAnswerComment(cursor, message):
    cursor.execute("""INSERT INTO comment (answer_id, message, submission_time, edited_count)
                      VALUES ((%s), (%s),(%s), 0);""", (id, message, dt))


# @database_common.connection_handler
# def showAnswerComment(cursor, id):
#     cursor.execute("""SELECT message
#                       FROM comment
#                       WHERE answer_id={};""".format(id))
#     answercomments = cursor.fetchall()
#     return answercomments
