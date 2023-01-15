# Program for delivering presents
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/14/2023

file_path = "/Users/yeato/Documents/git_projects/adventOfCode2015/day9/data.txt"
# file_path = "/Users/yeato/Documents/git_projects/adventOfCode2015/day9/data_test.txt"

# Function to find the shortest possible path in a traveling salesman problem
def find_shortest_path(node_dict):
    shortest_path = [float('inf')]
    visited_set = {}
    for dest in node_dict:
        visited_set.update({dest : 1})
        temp_path = shortest_dfs(node_dict, visited_set, dest, 0, shortest_path)
        if (temp_path < shortest_path[0]):
            shortest_path[0] = temp_path
        visited_set.pop(dest)
    return shortest_path[0]

# Function to do DFS to recursively find the shortest path covering all nodes
# returns the shortest possible total path length at each node
def shortest_dfs(node_dict, vis_dests, curr_node, curr_path_length, curr_min_path):
    # Base case: visited all nodes or current path is longer than current min
    if (len(vis_dests) == len(node_dict)):
        return curr_path_length
    elif curr_path_length > curr_min_path[0]:
        return curr_min_path[0]

    min_path = float('inf')

    # Otherwise, check all adjacent nodes to the current node that aren't in the visited
    # set and find the shortest path
    for path in node_dict.get(curr_node):
        if path not in vis_dests:
            vis_dests.update({path : 1})
            below_path = shortest_dfs(node_dict, vis_dests, path, curr_path_length + node_dict.get(curr_node).get(path), curr_min_path)
            vis_dests.pop(path)
            if below_path < min_path:
                min_path = below_path

    return min_path

# Function to find the longest possible path in a traveling salesman problem
def find_longest_path(node_dict):
    longest_path = [0]
    visited_set = {}
    for dest in node_dict:
        visited_set.update({dest : 1})
        temp_path = longest_dfs(node_dict, visited_set, dest, 0, longest_path)
        if (temp_path > longest_path[0]):
            longest_path[0] = temp_path
        visited_set.pop(dest)
    return longest_path[0]

# Function to do DFS to recursively find the longest path covering all nodes
# returns the longest total possible path length at any node
def longest_dfs(node_dict, vis_dests, curr_node, curr_path_length, curr_max_path):
    # Base case: visited all nodes or current path is longer than current min
    if (len(vis_dests) == len(node_dict)):
        return curr_path_length

    max_path = 0

    # Otherwise, check all adjacent nodes to the current node that aren't in the visited
    # set and find the longest path
    for path in node_dict.get(curr_node):
        if path not in vis_dests:
            vis_dests.update({path : 1})
            below_path = longest_dfs(node_dict, vis_dests, path, curr_path_length + node_dict.get(curr_node).get(path), curr_max_path)
            vis_dests.pop(path)
            if below_path > max_path:
                max_path = below_path

    return max_path


# ---------------------------------------------

f = open(file_path,'r')

path_dict = {}

for line in f:
    line = line.strip()
    split_line = line.split(" ")
    d1 = split_line[0]
    d2 = split_line[2]
    dist = int(split_line[4])
    path_dict.setdefault(d1,{})
    path_dict.get(d1).update({d2 : dist})
    path_dict.setdefault(d2,{})
    path_dict.get(d2).update({d1 : dist})

print(find_shortest_path(path_dict))
print(find_longest_path(path_dict))