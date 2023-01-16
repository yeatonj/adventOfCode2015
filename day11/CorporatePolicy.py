# Program for corporate policy
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/15/2023

# Functions
def increment_pw(pw_arr, banned):
    i = len(pw_arr) - 1
    complete = False
    while (not complete and i >= 0):
        pw_arr[i] += 1
        if pw_arr[i] > 25:
            pw_arr[i] -= 26
            i -= 1
        elif pw_arr[i] not in banned:
            complete = True

def check_pw(pw_arr):
    first_pair = False
    second_pair = False
    inc_straight = False
    num1 = None
    num2 = None
    for i in range(len(pw_arr)):
        curr_num = pw_arr[i]
        if num2 != None and num2 == curr_num:
            if not first_pair:
                first_pair = True
                first_pair_val = curr_num
            elif curr_num != first_pair_val:
                second_pair = True
        elif num1 != None and num2 == (curr_num - 1) and num1 == (num2 -1):
            inc_straight = True
        num1 = num2
        num2 = curr_num
    return (first_pair and second_pair and inc_straight)

def print_result(result_arr):
    out_str = ""
    for num in result_arr:
        out_str += chr(ord('a') + num)
    print(out_str)


#-----------------------------------
# Main Program

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day11/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day11/data_test.txt"

f = open(filepath,'r')
data = f.readline()

data_arr = []

for char in data:
    data_arr.append(ord(char) - ord('a'))

banned_nums = [ord('i') - ord('a'), ord('l') - ord('a'), ord('o') - ord('a')]

found = False
while not found:
    increment_pw(data_arr, banned_nums)
    found = check_pw(data_arr)

print_result(data_arr)

found = False
while not found:
    increment_pw(data_arr, banned_nums)
    found = check_pw(data_arr)

print_result(data_arr)

f.close()