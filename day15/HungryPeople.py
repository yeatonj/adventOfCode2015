# Program for reindeer games
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/10/2023

# Functions --------------------------------------

# Function to calculate score for a given mix of ingredients
def calc_score(weights, ing_mix):
    totals = [0,0,0,0] #capacity, durability, flavor, texture, cals
    for ing in ing_mix:
        curr_scores = weights.get(ing)
        num_ing = ing_mix.get(ing)
        totals[0] += curr_scores.get("capacity")*num_ing
        totals[1] += curr_scores.get("durability")*num_ing
        totals[2] += curr_scores.get("flavor")*num_ing
        totals[3] += curr_scores.get("texture")*num_ing
    total_score = 1
    for total in totals:
        if total < 0:
            total = 0
        total_score *= total
    return total_score

def calc_cals(weights, ing_mix):
    calories = 0
    for ing in ing_mix:
        num_ing = ing_mix.get(ing)
        calories += weights.get(ing).get("calories")*num_ing
    return calories

def ings_to_tuple(ing_order, curr_ings):
    return tuple(curr_ings.get(ing_order[i]) for i in range(len(ing_order)))


def find_max_score(weights, max_ing):
    starting_ings = {}
    max_scores = {}
    ing_order = []
    for ing in weights:
        starting_ings.update({ing:0})
        ing_order.append(ing)
    return rec_max_score(weights, max_ing, starting_ings, max_scores, ing_order)

def find_max_score_cal(weights, max_ing, cal):
    starting_ings = {}
    max_scores = {}
    ing_order = []
    for ing in weights:
        starting_ings.update({ing:0})
        ing_order.append(ing)
    return rec_max_score_cal(weights, max_ing, starting_ings, max_scores, ing_order, cal)

def rec_max_score(weights, max_ing, curr_ings, max_scores, ing_order):
    curr_tuple = ings_to_tuple(ing_order, curr_ings)
    # Memoization lookup
    if curr_tuple in max_scores:
        return max_scores.get(curr_tuple)
    # Base case - 
    elif sum(curr_tuple) == max_ing:
        curr_score = calc_score(weights,curr_ings)
        max_scores.update({curr_tuple:curr_score})
        return curr_score
    # Iterate through choices to find new max score
    max_score = 0
    for ing in ing_order:
        curr_count = curr_ings.get(ing)
        curr_ings.update({ing:curr_count+1})
        temp_max = rec_max_score(weights, max_ing, curr_ings, max_scores, ing_order)
        if temp_max > max_score:
            max_score = temp_max
        curr_ings.update({ing:curr_count})
    # Max score now is the maximum from all tests beneath this node, so update memoization
    max_scores.update({curr_tuple:max_score})
    return max_score

def rec_max_score_cal(weights, max_ing, curr_ings, max_scores, ing_order, cals):
    curr_tuple = ings_to_tuple(ing_order, curr_ings)
    # Memoization lookup
    if curr_tuple in max_scores:
        return max_scores.get(curr_tuple)
    # Base case - 
    elif sum(curr_tuple) == max_ing and cals == calc_cals(weights, curr_ings):
        curr_score = calc_score(weights,curr_ings)
        max_scores.update({curr_tuple:curr_score})
        return curr_score
    elif sum(curr_tuple) == max_ing:
        max_scores.update({curr_tuple:0})
        return 0
    # Iterate through choices to find new max score
    max_score = 0
    for ing in ing_order:
        curr_count = curr_ings.get(ing)
        curr_ings.update({ing:curr_count+1})
        temp_max = rec_max_score_cal(weights, max_ing, curr_ings, max_scores, ing_order, cals)
        if temp_max > max_score:
            max_score = temp_max
        curr_ings.update({ing:curr_count})
    # Max score now is the maximum from all tests beneath this node, so update memoization
    max_scores.update({curr_tuple:max_score})
    return max_score

# Main Program ---------------------------------------------------

MAX_ING = 100
CAL_MATCH = 500
filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day15/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day15/data_test.txt"

data = open(filepath, 'r')

weight_dict = {}

for line in data:
    data_line = line.strip().split(" ")
    curr_ingredient = data_line[0].strip(":")
    weight_dict.update({curr_ingredient:{}})
    for i in range(1,len(data_line),2):
        weight_dict.get(curr_ingredient).update({data_line[i]:int(data_line[i+1].strip(","))})

pt1_max = find_max_score(weight_dict, MAX_ING)
pt2_max = find_max_score_cal(weight_dict, MAX_ING, CAL_MATCH)

print("Part 1 solution is: " + str(pt1_max))
print("Part 2 solution is: " + str(pt2_max))