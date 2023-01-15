# Program for playing a word game with elves
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/15/2023

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day10/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day10/data_test.txt"

def look_and_say(s_in):
    i = 0
    prev_char = ""
    output_string = ""
    while i < len(s_in):
        curr_char = s_in[i]
        if (prev_char == ""):
            count = 1
            prev_char = s_in[0]
        elif (prev_char != curr_char):
            output_string += (str(count) + prev_char)
            count = 1
            prev_char = curr_char
        else:
            count += 1
        i += 1

    return (output_string  + str(count) + prev_char)

f = open(filepath,'r')
data = f.readline().strip()
f.close()

# Adjust this for part 1/ part 2
times_to_apply = 50

for i in range(times_to_apply):
    data = look_and_say(data)

print(len(data))