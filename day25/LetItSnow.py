# Program for fixing Santa's Machine
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/12/2023

# To find the iteration number:
# Row: (r,1) = 1 + 1 + 2 + 3 + ... + r-1
# Col: if (r,1) = n, (r, c) = n + (r+1) + (r+2) + ... + (r + c)

def iter_num(row, col):
    num = 1
    for i in range(1,row):
        num+=i
    for j in range(1,col):
        num+=row+j
    return num

# Main program
data_iteration = iter_num(3010,3019) - 1
curr_code = 20151125
for i in range(data_iteration):
    curr_code = (curr_code * 252533) % 33554393

print(curr_code)