import string


def read_input():
    with open('input.txt', 'r') as file:
        raw_data = file.readlines()
    return raw_data


def calculate_answers(raw_data):
    answergroup = set()
    answers = []

    for line in raw_data:
        if line == '\n':
            answers.append(answergroup)
            answergroup = set()
        else:

            for char in line.strip():
                answergroup.add(char)

    answers.append(answergroup)

    return answers


def calculate_answers2(raw_data):
    answers = []
    answer_count = dict.fromkeys(string.ascii_lowercase, 0)

    row_count = 0
    for line in raw_data:
        if line == '\n':
            answers.append((row_count, answer_count))
            answer_count = dict.fromkeys(string.ascii_lowercase, 0)
            row_count = 0
        else:
            row_count += 1
            for char in line.strip():
                answer_count[char] += 1

    answers.append((row_count, answer_count))

    return answers


answer_count = dict.fromkeys(string.ascii_lowercase, 0)


def process_answers(answers):
    for answergroup in answers:
        for char in answergroup:
            answer_count[char] += 1

    total = 0
    for key in answer_count:
        total += answer_count[key]

    return total


def process_answers2(answers):
    total = 0
    for (row_count, answer_count) in answers:
        for key in answer_count:
            if answer_count[key] == row_count:
                total += 1

    return total


input = read_input()
answers = calculate_answers2(input)
count = process_answers2(answers)
print(count)
