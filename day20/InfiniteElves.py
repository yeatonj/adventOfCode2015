# Program for Infinite Elves
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/10/2023

def find_factors(number):
    search_range = range(1,int(number**0.5)+1)
    facs = []
    for potential_fac in search_range:
        if number % potential_fac == 0:
            facs.append(potential_fac)
            if (number // potential_fac) not in facs:
                facs.append(number// potential_fac)
    if number % 2 == 0 and (number//2 not in facs):
        facs.append(number//2)
    if number not in facs:
        facs.append(number)
    facs.sort()
    return facs


filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day20/data.txt"
data = open(filepath,'r')
num = int(data.readline().strip())
data.close()

temp_sum = 0
i = 0



# # part 1
# while temp_sum < num:
#     i+=1
#     temp_sum = 0
#     facs = find_factors(i)
#     temp_sum = 10*sum(facs)

# part 2
while temp_sum < num:
    i+=1
    temp_sum = 0
    facs = find_factors(i)
    for factor in facs:
        if factor >= (i // 50):
            temp_sum += 11*factor

print(i)