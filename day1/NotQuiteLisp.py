# Class to determine floors that an elevator travels
# Written for Advent of Code 2015 (completed in 2022)
# Written by: Joshua Yeaton
# Written on: 1/8/2023

f = open("/Users/yeato/Documents/git_projects/adventOfCode2015/day1/data.txt", "r")
sum = 0
index = 1

data_in = f.read()
for char in data_in:
    if char == '(':
        sum += 1
    else:
        sum -= 1
    if sum == -1:
        print(index)
    index += 1
print(sum)