import csv
import actions


def read_questions(file_name="question.csv"):
    data = []
    with open(file_name, newline="") as data_file:
        datareader = csv.reader(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in datareader:
                row[4] = actions.base64_to_string(row[4])
                row[5] = actions.base64_to_string(row[5])
                data.append(row)
    return data


def read_answers(file_name="answer.csv"):
    data = []
    with open(file_name, newline="") as data_file:
        datareader = csv.reader(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in datareader:
                row[4] = actions.base64_to_string(row[4])
                data.append(row)
    return data


def append_question(new_question, file_name="question.csv"):
    new_question[4] = actions.string_to_base64(new_question[4])
    new_question[5] = actions.string_to_base64(new_question[5])
    with open(file_name, "a", newline="") as data_file:
        datawriter = csv.writer(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        datawriter.writerow(new_question)
    questions = read_questions("question.csv")
    return questions


def append_answer(new_answer, file_name="answer.csv"):
    new_answer[4] = actions.string_to_base64(new_answer[4])
    with open(file_name, "a", newline="") as data_file:
        datawriter = csv.writer(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        datawriter.writerow(new_answer)
    answers = read_answers("answer.csv")
    return answers
