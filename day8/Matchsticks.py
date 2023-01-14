# Program for checking strings
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/14/2023

# file_path = "/Users/yeato/Documents/git_projects/adventOfCode2015/day8/data_test.txt"
file_path = "/Users/yeato/Documents/git_projects/adventOfCode2015/day8/data.txt"

f = open(file_path,'r')

# Values for each answer, literal is what python prints, actual is what we would get if it
# were read correctly, and encoded is what it would cost to encode the literal
literal = 0
actual = 0
encoded = 0

for line in f:
    line = line.strip()
    line_len = len(line)
    literal += line_len
    i = 0
    while i < line_len:
        if line[i] == '\\':
            # Case - escape character found
            if line[i+1] == '"' or line[i+1] == "\\":
                # case, \\ or \"
                encoded += 4
                actual += 1
                i += 2
            else:
                # case, hex (\xhh)
                encoded += 5
                actual += 1
                i += 4
        elif line[i] != '"':
            # Case - regular number/letter/whatever
            encoded += 1
            actual += 1
            i += 1
        else:
            # Case - character is "
            encoded += 3
            i += 1

# Print answers
print("Literal: " + str(literal))
print("Actual: " + str(actual))
print("Encoded: " + str(encoded))
print("Literal - Actual: " + str(literal - actual))
print("Encoded - Literal: " + str(encoded - literal))
