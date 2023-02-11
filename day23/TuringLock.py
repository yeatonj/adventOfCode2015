# Program for Opening a Turing Lock
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/11/2023

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day23/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day23/data_test.txt"

# Read in and process the data
data = open(filepath,'r')
instructions = []
for line in data:
    line = line.strip().replace(",","").split(" ")
    if len(line) == 3:
        line[2] = int(line[2])
    elif line[0] == "jmp":
        line[1] = int(line[1])
    instructions.append(line)
data.close()

# Initialize values
# val_a = 0
val_a = 1
val_b = 0
reg_vals = [val_a,val_b]
curr_line = 0

# Loop through instructions
while (curr_line < len(instructions)):
    curr_ins = instructions[curr_line]
    # First, make sure we're not doing something regardless of register
    if curr_ins[0] == "jmp":
        curr_line += curr_ins[1]
        continue
    reg_indx = ord(curr_ins[1]) - ord('a')
    if curr_ins[0] == "hlf":
        reg_vals[reg_indx] //= 2
        curr_line += 1
    elif curr_ins[0] == "tpl":
        reg_vals[reg_indx] *= 3
        curr_line += 1
    elif curr_ins[0] == "inc":
        reg_vals[reg_indx] += 1
        curr_line += 1
    elif curr_ins[0] == "jie":
        if (reg_vals[reg_indx] % 2 == 0):
            curr_line += curr_ins[2]
        else:
            curr_line += 1
    elif curr_ins[0] == "jio":
        if (reg_vals[reg_indx] == 1):
            curr_line += curr_ins[2]
        else:
            curr_line += 1
    else:
        print("Missed an instruction")

print(reg_vals)
