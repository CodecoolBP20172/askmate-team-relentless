import csv
import time

'''
def get_question_list
    # sortolva a timestamp alapján
'''


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
    timestamp = int(time.time())
    return timestamp
