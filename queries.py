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
def question_limited(cursor):
    cursor.execute("""SELECT *
                      FROM question
                      ORDER BY id DESC
                      LIMIT 5;""")
    rows = cursor.fetchall()
    return rows


@database_common.connection_handler
def show_question(cursor, id):
    cursor.execute("""SELECT *
                      FROM question
                      WHERE id=%s""", (id,))
    question = cursor.fetchall()
    return question


@database_common.connection_handler
def show_answers(cursor, id):
    cursor.execute("""SELECT *
                      FROM answer
                      WHERE question_id=%s""", (id,))
    answers = cursor.fetchall()
    return answers


@database_common.connection_handler
def add_new_question(cursor, title, message, pick_user):
    cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_name)
                      VALUES ((%s), 0, 0, (%s), (%s), '', (%s));""", (my_format.format(datetime.now()), title, message, pick_user))


@database_common.connection_handler
def add_new_answer(cursor, id, message, user_name):
    cursor.execute("""INSERT INTO answer (submission_time, vote_number, question_id, message, image, user_name)
                      VALUES ((%s), 0, (%s), (%s), '', (%s));""", (my_format.format(datetime.now()), id, message, user_name))


@database_common.connection_handler
def add_new_question_comment(cursor, id, message):
    cursor.execute("""INSERT INTO comment (question_id, message, submission_time, edited_count)
                      VALUES ((%s), (%s),(%s), 0);""", (id, message, my_format.format(datetime.now())))


@database_common.connection_handler
def show_question_comment(cursor, id):
    cursor.execute("""SELECT message
                      FROM comment
                      WHERE question_id=%s""", (id,))
    comments = cursor.fetchall()
    return comments


@database_common.connection_handler
def register_user(cursor, new_name):
    cursor.execute("""INSERT INTO username(user_name, submission_time)
                      VALUES ((%s), (%s))
                      ON CONFLICT DO NOTHING;""", (new_name, my_format.format(datetime.now())))


@database_common.connection_handler
def list_users(cursor):
    cursor.execute("""SELECT user_name, submission_time
                      FROM username
                      ORDER BY id DESC;""")
    users = cursor.fetchall()
    return users
