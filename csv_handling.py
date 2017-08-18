import csv
import base64


def base64_to_string(encoded_string):
    decoded_string = base64.b64decode(encoded_string)
    return decoded_string.decode('utf-8')


def string_to_base64(origin):
    origin_in_bytes = origin.encode('utf-8')
    b64_encoded_bytes = base64.b64encode(origin_in_bytes)
    return b64_encoded_bytes.decode('utf-8')


def read_questions(file_name="question.csv"):
    data = []
    with open(file_name, newline="") as data_file:
        datareader = csv.reader(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in datareader:
                data.append(row)
    return data


def read_answers(file_name="answer.csv"):
    data = []
    with open(file_name, newline="") as data_file:
        datareader = csv.reader(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in datareader:
                data.append(row)
    return data


def append_question(new_question, file_name="question.csv"):
    with open(file_name, "a", newline="") as data_file:
        datawriter = csv.writer(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        datawriter.writerow(new_question)
    questions = read_questions("question.csv")
    return questions


def append_answer(new_answer, file_name="answer.csv"):
    with open(file_name, "a", newline="") as data_file:
        datawriter = csv.writer(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        datawriter.writerow(new_answer)
    answers = read_answers("answer.csv")
    return answers
