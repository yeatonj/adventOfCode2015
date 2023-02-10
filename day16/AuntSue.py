# Program for Forensics
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/10/2023

# Read in the MFCSAM data
filepath_actual = "/Users/yeato/Documents/git_projects/adventOfCode2015/day16/actual.txt"
data_actual = open(filepath_actual, 'r')
actual_dict = {}
for line in data_actual:
    split_data = line.strip().split(": ")
    actual_dict.update({split_data[0]:int(split_data[1])})
data_actual.close()

# Look through the sues for part 1
filepath_data = "/Users/yeato/Documents/git_projects/adventOfCode2015/day16/data.txt"
sue_data = open(filepath_data,'r')
for sue in sue_data:
    sue_n = sue.replace(':','').replace(',','').strip().split()
    found = True
    for i in range(2,len(sue_n),2):
        field = sue_n[i]
        num = int(sue_n[i+1])
        if actual_dict.get(field) != num:
            found = False
            break
    if found:
        print("Found match, Sue number: " + str(sue_n[1]))
sue_data.close()

# Look through the sues for part 2
def check_pt2(actual_data, check_sue):
    for i in range(2,len(check_sue),2):
        field = check_sue[i]
        num = int(check_sue[i+1])
        if (field == "cats" or field == "trees"):
            if num <= actual_data.get(field):
                return False
        elif (field == "pomeranians" or field == "goldfish"):
            if num >= actual_data.get(field):
                return False
        elif actual_data.get(field) != num:
            return False
    return True

filepath_data = "/Users/yeato/Documents/git_projects/adventOfCode2015/day16/data.txt"
sue_data = open(filepath_data,'r')
for sue in sue_data:
    sue_n = sue.replace(':','').replace(',','').strip().split()
    found = check_pt2(actual_dict, sue_n)
    if found:
        print("Found match, Sue number: " + str(sue_n[1]))
sue_data.close()