# Program for interpreting JSON
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/16/2023

import re
import json

#----------------------------------
# Functions

def json_sum(json_dict, ignore = None):
    return recursive_sum(json_dict, ignore)

def recursive_sum(json_data, ignore):
    temp_sum = 0
    if type(json_data) is dict:
        if (ignore != None and ignore in json_data.values()):
            return 0
        for value in json_data.values():
            try:
                temp_sum += int(value)
            except:
                temp_sum += recursive_sum(value, ignore)
    elif type(json_data) is list:
        for value in json_data:
            try:
                temp_sum += int(value)
            except:
                temp_sum += recursive_sum(value, ignore)
    else:
        try:
            temp_sum += int(json_data)
        except:
            pass

    return temp_sum

#-----------------------------------
# Main Program

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day12/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day12/data_test.txt"

f = open(filepath,'r')
data = f.readline()

js_data = json.loads(data)

print(json_sum(js_data))

print(json_sum(js_data, 'red'))