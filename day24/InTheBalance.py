# Program for calculating packet weights
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/16/2023

import queue

def find_sums_with_els(w_list, w_target, num_els):
    solutions = []
    ans_queue = queue.Queue()
    ans_queue.put([])
    ans_queue.put([w_list[0]])
    for i in range(1,len(w_list)):
        next_weight = w_list[i]
        # Create a temporary new queue
        temp_queue = queue.Queue()
        while not ans_queue.empty():
            curr_comb = ans_queue.get()
            rem_chars = num_els - len(curr_comb)
            max_rem_weight = sum(w_list[i:i+rem_chars])
            curr_sum = sum(curr_comb)
            if curr_sum + max_rem_weight < w_target:
                continue
            elif curr_sum + next_weight == w_target and (len(curr_comb) == (num_els - 1)):
                soln_comb = curr_comb.copy()
                soln_comb.append(next_weight)
                solutions.append(soln_comb)
            elif (curr_sum + next_weight < w_target) and (len(curr_comb) < (num_els - 1)):
                new_comb = curr_comb.copy()
                new_comb.append(next_weight)
                temp_queue.put(new_comb)
            temp_queue.put(curr_comb)
        ans_queue = temp_queue
    if solutions != []:
        return solutions
    return False

def find_valid_solutions(w_list, sol_list, w_target):
    valid_sols = []
    for sol in sol_list:
        found = False
        rem_weights = w_list.copy()
        # remove the used weights from the list
        for weight in sol:
            rem_weights.remove(weight)
        # Now, check to see if there is ANY valid way to get to the target with remaining weights
        # if so, the others also add to the target and this is a valid solution
        ans_queue = queue.Queue()
        ans_queue.put([])
        ans_queue.put([rem_weights[0]])
        for i in range(1,len(rem_weights)):
            next_weight = rem_weights[i]
            # Create a temporary new queue
            temp_queue = queue.Queue()
            while not ans_queue.empty():
                if found:
                    break
                curr_comb = ans_queue.get()
                max_rem_weight = sum(rem_weights[i:])
                curr_sum = sum(curr_comb)
                if curr_sum + max_rem_weight < w_target:
                    continue
                elif curr_sum + next_weight == w_target:
                    valid_sols.append(sol)
                    found = True
                    continue
                elif (curr_sum + next_weight < w_target):
                    new_comb = curr_comb.copy()
                    new_comb.append(next_weight)
                    temp_queue.put(new_comb)
                temp_queue.put(curr_comb)
            ans_queue = temp_queue
    if valid_sols != []:
        return valid_sols
    return False

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day24/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day24/data_test.txt"

data = open(filepath,'r')
weights = []
for line in data:
    weights.append(int(line.strip()))
data.close()

# Find the target for our algorithm
# target = sum(weights)//3 # swap comments for pt1 and pt2
target = sum(weights)//4
weights.sort(reverse=True)

# Look for 1 element sums, then 2, then 3, etc.
for i in range(len(weights)):
    if sum(weights[:i+1]) < target:
        continue
    curr_sols = find_sums_with_els(weights, target, i)
    if curr_sols:
        print("Found " + str(len(curr_sols)) + " possible solutions for " + str(i) + " packages.")
        valid_sols = find_valid_solutions(weights,curr_sols,target)
        if valid_sols:
            print("Found " + str(len(valid_sols)) + " valid solutions for " + str(i) + " packages.")
            products = []
            for soln in valid_sols:
                prod = 1
                for num in soln:
                    prod *= num
                products.append(prod)
            products.sort()
            print("Smallest QE is: " + str(products[0]) + ".")
            break
                
