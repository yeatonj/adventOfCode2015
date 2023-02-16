# Program for calculating packet weights
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/16/2023

import queue
import copy

# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day24/data.txt"
filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day24/data_test.txt"

data = open(filepath,'r')
weights = []
for line in data:
    weights.append(int(line.strip()))
data.close()

# Find the target for our algorithm
target = sum(weights)//3
weights.sort(reverse=True)

# At each step, choose to either take or leave each weight, starting with the first.
# Base case 1: we hit the target weight
# Base case 2: we exceed the target weight
# Base case 3: we run out of weights to add
# Use a queue-based system
cont_queue = queue.Queue()
# This will store the combinations that sum to the correct weights
correct_combos = []
# Add the first two options to initialize the queue
cont_queue.put([[weights.copy()[0]], weights.copy()[1:]])
cont_queue.put([[], weights.copy()])
for i in range(1,len(weights)):
    # Find total remaining weight - early exit to program and trims queue
    total_rem_weight = sum(weights[i:])
    next_weight = weights[i]
    # Create a temporary new queue
    temp_queue = queue.Queue()
    # Poll the queue for each option and take/do not take each weight
    counter = 0
    while not cont_queue.empty():
        curr_combo = cont_queue.get()
        curr_sum = sum(curr_combo[0])
        # Skip this if we can't possibly hit the target
        if curr_sum + total_rem_weight < target:
            continue
        elif curr_sum + next_weight == target:
            corr_combo = copy.deepcopy(curr_combo)
            corr_combo[0].append(next_weight)
            corr_combo[1].remove(next_weight)
            correct_combos.append(corr_combo)
        elif curr_sum + next_weight < target:
            new_combo = copy.deepcopy(curr_combo)
            new_combo[0].append(next_weight)
            new_combo[1].remove(next_weight)
            temp_queue.put(new_combo)
        temp_queue.put(curr_combo)
    cont_queue = temp_queue

final_combos = []

for entry in correct_combos:
    rem_list = entry[1]

# print(len(correct_combos))
print("Done")