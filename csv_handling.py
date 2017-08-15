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
        datareader = csv.reader(data_file, delimiter=",", quotechar="|")
        for row in datareader:
            row[3] = base64_to_string(row[3])
            row[4] = base64_to_string(row[4])
            row[5] = base64_to_string(row[5])
            data.append(row)
    return data


def read_answers(file_name="answer.csv"):
    data = []
    with open(file_name, newline="") as data_file:
        datareader = csv.reader(data_file, delimiter=",", quotechar="|")
        for row in datareader:
            row[4] = base64_to_string(row[4])
            row[5] = base64_to_string(row[5])
            data.append(row)
    return data


def append_question(new_question, file_name="question.csv"):
    with open(file_name, "a", newline="") as data_file:
        datawriter = csv.writer(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        new_question[3] = string_to_base64(new_question[3])
        new_question[4] = string_to_base64(new_question[4])
        new_question[5] = string_to_base64(new_question[5])
        datawriter.writerow(new_question)
    questions = read_data("question.csv")
    return questions


def append_answer(new_answer, file_name="answer.csv"):
    with open(file_name, "a", newline="") as data_file:
        datawriter = csv.writer(data_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        new_answer[4] = string_to_base64(new_answer[4])
        new_answer[5] = string_to_base64(new_answer[5])
        datawriter.writerow(new_answer)
    answers = read_data("answer.csv")
    return answers


# def print_info(variable):
#     print("Original string: {var} ({type})".format(**{
#         "var": variable,
#         "type": type(variable)
#     }))

# original_string = "Test string"
# encoded_string = string_to_base64(original_string)
# decoded_string = base64_to_string(encoded_string)


# # Check if we have strings in all variables
# print_info(original_string)
# print_info(encoded_string)
# print_info(decoded_string)
