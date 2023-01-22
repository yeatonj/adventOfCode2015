# Program for calculating seating arrangements
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/21/2023

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day13/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day13/data_test.txt"

def find_max(base_seats, hap_dict):
    visited_seats = [base_seats[0]]
    return recursive_seats(visited_seats, hap_dict)

def recursive_seats(seated_guests, hap_dict):
    curr_seated = len(seated_guests)
    if curr_seated == len(hap_dict):
        right = hap_dict.get(seated_guests[curr_seated - 1]).get(seated_guests[0])
        left = hap_dict.get(seated_guests[0]).get(seated_guests[curr_seated - 1])
        return right + left
    curr_max = float('-inf')
    for guest in hap_dict.get(seated_guests[curr_seated - 1]):
        if guest not in seated_guests:
            seated_guests.append(guest)
            right = hap_dict.get(seated_guests[curr_seated - 1]).get(guest)
            left = hap_dict.get(guest).get(seated_guests[curr_seated - 1])
            temp = right + left + recursive_seats(seated_guests, hap_dict)
            seated_guests.pop(curr_seated)
            if temp > curr_max:
                curr_max = temp
    return curr_max

f = open(filepath,'r')
data = {}

for line in f:
    line = line.strip().replace('.', ' ')
    split_line = line.split(" ")
    units = int(split_line[3])
    if split_line[2] == 'lose':
        units *= -1
    data.setdefault(split_line[0],{})
    data.get(split_line[0]).update({split_line[10]:units})

# Generate the base list
base_seats = []
for key in data:
    base_seats.append(key)

# Part 1
pt1 = find_max(base_seats, data)
print(pt1)

#Part 2
data.update({'me':{}})
for person in data:
    data.get(person).update({'me':0})
    data.get('me').update({person:0})

pt2 = find_max(base_seats,data)
print(pt2)