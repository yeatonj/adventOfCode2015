# Program for healing Rudolph
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 2/11/2023

import re
import heapq

def num_matches(str1, str2):
    if len(str1) > len(str2):
        return 0
    i = 0
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        i+=1
    return i

def find_shortest_path(start, finish, matches):
    search_queue = [(0,start,0)]
    heapq.heapify(search_queue) # convert to a heap
    curr_mol = start
    searched_set = set()
    while (curr_mol != finish):
        first_el = heapq.heappop(search_queue)
        curr_mol = first_el[1]
        if curr_mol in searched_set:
            continue
        print(curr_mol)
        print("")
        searched_set.add(curr_mol)
        curr_steps = first_el[2]
        unique_new_mols = set()
        for match in matches:
            rep_indices = re.finditer(match[0],curr_mol)
            for rep in rep_indices:
                new_mol = curr_mol[:rep.start()] + match[1] + curr_mol[rep.end():]
                unique_new_mols.add(new_mol)
        for mol in unique_new_mols:
            char_match = -1 * num_matches(mol,finish)
            weight = char_match + len(mol)
            heapq.heappush(search_queue,(weight, mol, curr_steps + 1))
    return curr_steps

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day19/data.txt"
mol_filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day19/mol_data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day19/data_test.txt"
# mol_filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day19/mol_data_test.txt"

# Load molecule
mol_data = open(mol_filepath,'r')
mol = mol_data.readline().strip()
mol_data.close()

# Create a set for the new molecules
single_rep = set()

# Iterate through replacements, then add new molecules to set
data = open(filepath,'r')
reps = []
for poss_rep in data:
    poss_rep = poss_rep.strip().split(" => ")
    reps.append(poss_rep)
    rep_indices = re.finditer(poss_rep[0],mol)
    for rep in rep_indices:
        new_str = mol[:rep.start()] + poss_rep[1] + mol[rep.end():]
        single_rep.add(new_str)
data.close()
print(len(single_rep))
pt2 = find_shortest_path('e',mol,reps)
print(pt2)

