# Program where there was supposed to be no math
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/8/2023

f = open("/Users/yeato/Documents/git_projects/adventOfCode2015/day2/data.txt", "r")
paper_sum = 0
ribbon_sum = 0

def find_sides(present_dims):
    length = int(present_dims[0])
    width = int(present_dims[1])
    height = int(present_dims[2])
    return [length, width, height]

def paper_needed(present_dims):
    sides = find_sides(present_dims)
    length = sides[0]
    width = sides[1]
    height = sides[2]
    side_one = length * width
    side_two = length * height
    side_three = width * height
    min_side = side_one
    if (side_two < min_side):
        min_side = side_two
    if (side_three < min_side):
        min_side = side_three
    return 2*side_one + 2* side_two + 2*side_three + min_side

def ribbon_needed(present_dims):
    sides = find_sides(present_dims)
    print(sides)
    volume = 1
    for side in sides:
        volume*=side
    print(volume)

    max_side = sides[0]
    if (sides[1] > max_side):
        max_side = sides[1]
    if (sides[2] > max_side):
        max_side = sides[2]
    perim = sum(sides)
    perim -= max_side
    print(perim)
    print((perim*2) + volume)

    return (perim*2) + volume
    

for present in f:
    present = present.strip()
    dims = present.split('x')
    paper_sum += paper_needed(dims)
    ribbon_sum += ribbon_needed(dims)

print(paper_sum)
print(ribbon_sum)

# Answer of 31097025782 is too high


