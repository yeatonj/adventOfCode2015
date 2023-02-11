# Program for Animating a Yard
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/11/2023

# Function to print output and return lights on
def print_output(yard):
    total_on = 0
    for row in yard:
        for c in row:
            if c == '#':
                total_on += 1
            print(c,end="")
        print("")
    return total_on

# Function to get the number of lit neighbors to a cell
def get_lit_neigh(yard, r, c):
    height = len(yard)
    width = len(yard[0])
    total_lit = 0
    for i in range(r-1, r+2, 1):
        for j in range(c-1, c+2, 1):
            if i < 0 or j < 0 or i > height - 1 or j > width - 1:
                total_lit += 0
            elif i == r and j == c:
                total_lit += 0
            elif yard[i][j] == '#':
                total_lit +=1
            else:
                total_lit += 0
    return total_lit
                 

# Function to update the state of the yard
def update_state(yard):
    new_yard = []
    for i in range(len(yard)):
        new_row = []
        for j in range(len(yard[i])):
            lit_neigh = get_lit_neigh(yard,i,j)
            if yard[i][j] == '#' and (lit_neigh == 2 or lit_neigh == 3):
                new_row.append('#')
            elif yard[i][j] == '.' and lit_neigh == 3:
                new_row.append('#')
            else:
                new_row.append('.')
        new_yard.append(new_row)
    return new_yard

# part 2 update for state
def update_state_pt2(yard):
    new_yard = []
    for i in range(len(yard)):
        new_row = []
        for j in range(len(yard[i])):
            lit_neigh = get_lit_neigh(yard,i,j)
            if (i == 0 and (j == 0 or j == len(yard[i])-1)) or \
                (i == (len(yard) - 1) and (j == 0 or j == len(yard[i])-1)):
                new_row.append('#')
            elif yard[i][j] == '#' and (lit_neigh == 2 or lit_neigh == 3):
                new_row.append('#')
            elif yard[i][j] == '.' and lit_neigh == 3:
                new_row.append('#')
            else:
                new_row.append('.')
        new_yard.append(new_row)
    return new_yard

# ---------------- Main Program ---------------------------
filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day18/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day18/data_test.txt"

initial_state = []
data = open(filepath,'r')
for line in data:
    temp_line = []
    for c in line.strip():
        temp_line.append(c)
    initial_state.append(temp_line)
data.close()

NUM_STEPS = 100
new_state=update_state(initial_state)
for i in range(NUM_STEPS-1):
    new_state = update_state(new_state)
a = print_output(new_state)
print(a)

pt2_initial_state = initial_state.copy()
pt2_initial_state[0][0] = '#'
pt2_initial_state[len(pt2_initial_state) -1][0] = '#'
pt2_initial_state[0][len(pt2_initial_state[0])-1] = '#'
pt2_initial_state[len(pt2_initial_state) -1][len(pt2_initial_state[0]) -1] = '#'
pt2_new_state=update_state_pt2(pt2_initial_state)
for i in range(NUM_STEPS-1):
    pt2_new_state = update_state_pt2(pt2_new_state)
a = print_output(pt2_new_state)
print(a)