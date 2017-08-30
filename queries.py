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
def addNewQuestion(cursor, title, message):
    cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message, image)
                      VALUES ((%s), 0, 0, (%s), (%s), '');""", (dt, title, message))
