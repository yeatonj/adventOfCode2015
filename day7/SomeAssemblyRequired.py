# Program for performing some assembly
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/12/2023

def not_op(cur_line, answers):
    if cur_line[1].isdigit():
        answers.update({cur_line[1] : int(cur_line[1])})
    if cur_line[1] in answers and cur_line[3] not in answers:
        answers.update({cur_line[3] : ~answers.get(cur_line[1]) % NUM_BITS})

def and_op(cur_line, answers):
    if cur_line[0].isdigit():
        answers.update({cur_line[0] : int(cur_line[0])})
    if cur_line[2].isdigit():
        answers.update({cur_line[2] : int(cur_line[2])})
    if cur_line[0] in answers and cur_line[2] in answers and cur_line[4] not in answers:
        answers.update({cur_line[4] : answers.get(cur_line[0]) & answers.get(cur_line[2]) % NUM_BITS})

def or_op(cur_line, answers):
    if cur_line[0].isdigit():
        answers.update({cur_line[0] : int(cur_line[0])})
    if cur_line[2].isdigit():
        answers.update({cur_line[2] : int(cur_line[2])})
    if cur_line[0] in answers and cur_line[2] in answers and cur_line[4] not in answers:
        answers.update({cur_line[4] : answers.get(cur_line[0]) | answers.get(cur_line[2]) % NUM_BITS})

def lshift_op(cur_line, answers):
    if cur_line[0].isdigit():
        answers.update({cur_line[0] : int(cur_line[0])})
    if cur_line[0] in answers and cur_line[4] not in answers:
        answers.update({cur_line[4] : answers.get(cur_line[0]) << int(cur_line[2]) % NUM_BITS})

def rshift_op(cur_line, answers):
    if cur_line[0].isdigit():
        answers.update({cur_line[0] : int(cur_line[0])})
    if cur_line[0] in answers and cur_line[4] not in answers:
        answers.update({cur_line[4] : answers.get(cur_line[0]) >> int(cur_line[2]) % NUM_BITS})

file_path = "/Users/yeato/Documents/git_projects/adventOfCode2015/day7/data.txt"

f = open(file_path)
data_lines = []
NUM_BITS = 65536

i = 0
for line in f:
    line = line.strip()
    split_line = line.split(" ")
    data_lines.append(split_line)

answers = {}

i = 0
while 'a' not in answers:
    cur_ind = i % len(data_lines)
    cur_line = data_lines[cur_ind]
    # direct wire
    if len(cur_line) == 3:
        try:
            answers.update({cur_line[2] : int(cur_line[0]) % NUM_BITS})
        except:
            if cur_line[0] in answers:
                answers.update({cur_line[2] : answers.get(cur_line[0])})
    # NOT
    if cur_line[0] == 'NOT':
        not_op(cur_line, answers)
    # AND
    elif cur_line[1] == 'AND':
        and_op(cur_line, answers)
    # OR
    elif cur_line[1] == 'OR':
        or_op(cur_line, answers)
    # LSHIFT
    elif cur_line[1] == 'LSHIFT':
        lshift_op(cur_line, answers)
    # RSHIFT
    elif cur_line[1] == 'RSHIFT':
        rshift_op(cur_line, answers)

    # print(answers)
    i += 1

print(answers.get('a'))
# For part 2, simply go into data and update b to result, then re-run part 1 code