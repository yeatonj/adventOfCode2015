# Program for Eggnog
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/10/2023

def check(poss_conts, rem_liq):
    min_cont = [float('inf'), 0]
    total = recursive_check(poss_conts, rem_liq, [], min_cont)
    return (total, min_cont[1])


def recursive_check(poss_conts, rem_liq, curr_conts, curr_min_cont):
    # curr_min_cont is [num_containers, num_combinations]
    # base cases
    if rem_liq == 0:
        if len(curr_conts) < curr_min_cont[0]:
            curr_min_cont[0] = len(curr_conts)
            curr_min_cont[1] = 1
        elif len(curr_conts) == curr_min_cont[0]:
            curr_min_cont[1] += 1
        return 1
    elif rem_liq < 0 or not poss_conts:
        return 0
    poss_conts_1 = poss_conts[1:].copy()
    new_conts_1 = curr_conts.copy()
    new_conts_1.append(poss_conts[0])
    poss_conts_2 = poss_conts[1:].copy()
    new_conts_2 = curr_conts.copy()
    return recursive_check(poss_conts_1, rem_liq - poss_conts[0], new_conts_1, curr_min_cont) + recursive_check(poss_conts_2, rem_liq, new_conts_2, curr_min_cont)

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day17/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day17/data_test.txt"

# TARGET = 25
TARGET = 150

containers = []
data = open(filepath, 'r')
for line in data:
    containers.append(int(line.strip()))
data.close()
containers.sort(reverse=True)

combs_min_containers = check(containers, TARGET)
print("Total combos: " + str(combs_min_containers[0]))
print("Ways for min containers: " + str(combs_min_containers[1]))