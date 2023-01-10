# Program for mining AdventCoins
# Written for Advent of Code 2015 (completed in 2022)
# Written by: Joshua Yeaton
# Written on: 1/10/2023

import hashlib

f = open("C:\\Users\\yeato\\git_projects\\adventOfCode2015\\day4\\data.txt")

str_in = f.readline()
hash_input = str_in
soln = ""

i = -1

# while not soln.startswith("00000"):
while not soln.startswith("000000"):
    i += 1
    hash_input = str_in + str(i)
    soln = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
    if (i % 100 == 0):
        print(hash_input)

print(soln)
print(i)