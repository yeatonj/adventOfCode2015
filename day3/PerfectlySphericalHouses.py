# Program for modeling deliveries to houses
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/9/2023

def update_loc(current_loc, direction):
    if direction == '^':
        return (current_loc[0], current_loc[1] + 1)
    elif direction == 'v':
        return (current_loc[0], current_loc[1] - 1)
    elif direction == '>':
        return (current_loc[0] + 1, current_loc[1])
    else:
        return (current_loc[0] - 1, current_loc[1])

f = open("C:\\Users\\yeato\\git_projects\\adventOfCode2015\\day3\\data.txt", "r")

directions = f.readline()
f.close()

current_loc = (0,0)
visited_dic = {current_loc:True}

for el in directions:
    current_loc = update_loc(current_loc, el)
    visited_dic.setdefault(current_loc, True)

print(len(visited_dic))

f = open("C:\\Users\\yeato\\git_projects\\adventOfCode2015\\day3\\data.txt", "r")

directions = f.readline()
f.close()

santa_current_loc = (0,0)
robot_current_loc = (0,0)
pt2_visited_dic = visited_dic = {santa_current_loc:True}

i = 1
for el in directions:
    if i % 2 == 1:
        santa_current_loc = update_loc(santa_current_loc, el)
        pt2_visited_dic.setdefault(santa_current_loc, True)
    else:
        robot_current_loc = update_loc(robot_current_loc, el)
        pt2_visited_dic.setdefault(robot_current_loc, True)
    i += 1

print(len(pt2_visited_dic))