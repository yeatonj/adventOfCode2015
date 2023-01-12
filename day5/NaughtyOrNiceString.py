# Program for checking if a string is naughty or nice
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/10/2023

# returns true if a string is naughty
def naughty_check(bad_words, line_in):
    duplicate = False
    bad_word = False
    vowels = "aeiou"
    letter_dict = {}
    for i in range(len(line_in)):
        curr_count = letter_dict.setdefault(line_in[i], 0)
        letter_dict.update({line_in[i]:curr_count + 1})
        if i < len(line_in) - 1:
            two_let = line_in[i] + line_in[i+1]
            if not duplicate:
                duplicate = check_duplicate(two_let)
            if not bad_word and two_let in bad_words:
                bad_word = True

    vowel_count = 0
    for char in vowels:
        vowel_count += letter_dict.setdefault(char, 0)

    return not ((vowel_count >=3) and (not bad_word) and (duplicate))

# returns true if duplicate letters are found
def check_duplicate(two_letters):
    if (two_letters[0] == two_letters[1]):
        return True
    return False

# returns true if the word is naughty
def pt2_naughty_check(line_in):
    letter_pair = False
    skip_letter = False
    prev_word = ""
    double_dict = {}
    for i in range(len(line_in) - 1):
        # Check for the first condition
        temp_word = line_in[i] + line_in[i+1]
        if not letter_pair and temp_word != prev_word:
            num = double_dict.setdefault(temp_word, 0)
            if num > 0:
                letter_pair = True
            else:
                double_dict.update({temp_word:num + 1})
        elif (temp_word == prev_word):
            temp_word = ""
        prev_word = temp_word
        # check for the second condition
        if not skip_letter and i < len(line_in) - 2:
            if line_in[i] == line_in[i+2]:
                skip_letter = True
    return not (letter_pair and skip_letter)

        


naughty_words = {"ab":1, "cd":1, "pq":1, "xy":1}

f = open("/Users/yeato/Documents/git_projects/adventOfCode2015/day5/data.txt","r")

total = 0
for line in f:
    total += not naughty_check(naughty_words, line.strip())

f.close()
print(total)
        
f = open("/Users/yeato/Documents/git_projects/adventOfCode2015/day5/data.txt","r")

# part 2
total = 0
for line in f:
    total += not pt2_naughty_check(line.strip())
f.close()
print("Total is " + str(total))
# 68 was not the correct answer
