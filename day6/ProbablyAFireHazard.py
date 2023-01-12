# Program for checking for fire hazards
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/10/2023

def turn_on(light_array, instr_line):
    start_coord = instr_line[2].split(",")
    end_coord = instr_line[4].split(",")
    x_range = range(int(start_coord[0]), int(end_coord[0]) + 1)
    y_range = range(int(start_coord[1]), int(end_coord[1]) + 1)
    for i in x_range:
        for j in y_range:
            light_array[i][j] = 1

def turn_on_pt2(light_array, instr_line):
    start_coord = instr_line[2].split(",")
    end_coord = instr_line[4].split(",")
    x_range = range(int(start_coord[0]), int(end_coord[0]) + 1)
    y_range = range(int(start_coord[1]), int(end_coord[1]) + 1)
    for i in x_range:
        for j in y_range:
            light_array[i][j] += 1

def turn_off(light_array, instr_line):
    start_coord = instr_line[2].split(",")
    end_coord = instr_line[4].split(",")
    x_range = range(int(start_coord[0]), int(end_coord[0]) + 1)
    y_range = range(int(start_coord[1]), int(end_coord[1]) + 1)
    for i in x_range:
        for j in y_range:
            light_array[i][j] = 0

def turn_off_pt2(light_array, instr_line):
    start_coord = instr_line[2].split(",")
    end_coord = instr_line[4].split(",")
    x_range = range(int(start_coord[0]), int(end_coord[0]) + 1)
    y_range = range(int(start_coord[1]), int(end_coord[1]) + 1)
    for i in x_range:
        for j in y_range:
            if light_array[i][j] > 0:
                light_array[i][j] -= 1

def toggle(light_array, instr_line):
    start_coord = instr_line[1].split(",")
    end_coord = instr_line[3].split(",")
    x_range = range(int(start_coord[0]), int(end_coord[0]) + 1)
    y_range = range(int(start_coord[1]), int(end_coord[1]) + 1)
    for i in x_range:
        for j in y_range:
            if light_array[i][j] == 0:
                light_array[i][j] = 1
            else:
                light_array[i][j] = 0

def toggle_pt2(light_array, instr_line):
    start_coord = instr_line[1].split(",")
    end_coord = instr_line[3].split(",")
    x_range = range(int(start_coord[0]), int(end_coord[0]) + 1)
    y_range = range(int(start_coord[1]), int(end_coord[1]) + 1)
    for i in x_range:
        for j in y_range:
            light_array[i][j] += 2

data_file = "/Users/yeato/Documents/git_projects/adventOfCode2015/day6/data.txt"

f = open(data_file,'r')

NUM_LIGHTS = 1000
light_array = [[0]*NUM_LIGHTS for i in range(NUM_LIGHTS)]
for i in range(NUM_LIGHTS):
    for j in range(NUM_LIGHTS):
        light_array[i][j] = 0

for line in f:
    line = line.strip()
    split_line = line.split(" ")
    if split_line[1] == "on":
        # turn_on(light_array, split_line)
        turn_on_pt2(light_array, split_line)
    elif split_line[1] == "off":
        # turn_off(light_array, split_line)
        turn_off_pt2(light_array, split_line)
    else:
        # toggle(light_array, split_line)
        toggle_pt2(light_array, split_line)


lights_on = 0
for i in range(NUM_LIGHTS):
    for j in range(NUM_LIGHTS):
        lights_on += light_array[i][j]

print(lights_on)
f.close()