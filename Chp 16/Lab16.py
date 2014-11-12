import re

# Function to split text into checkable words
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

# Read and store dictionary as list
dictionary = open("dictionary.txt")
dictionary_list = []
for line in dictionary:
    line = line.strip()
    dictionary_list.append(line)
dictionary.close()

# Linear Search Spell Check
print("--- Linear Search ---")
file = open("AliceInWonderland200.txt")
line_number = 0
for line in file:
    words = split_line(line)
    line_number += 1
    for word in words:
        i = 0
        while i < len(dictionary_list) and dictionary_list[i] != word.upper():
            i += 1
        if i == len(dictionary_list):
            print("Line " + str(line_number) + " possible misspelled word: " + word) 
file.close()

# Binary Search Spell Check
print("--- Binary Search ---")
file = open("AliceInWonderland200.txt")
line_number = 0
for line in file:
    words = split_line(line)
    line_number += 1
    for word in words:
        desired_element = word.upper()
        lower_bound = 0
        upper_bound = len(dictionary_list)-1
        found = False
        while lower_bound <= upper_bound and found == False:
            middle_pos = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_pos] < desired_element:
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > desired_element:
                upper_bound = middle_pos - 1
            else:
                found = True
        if found == False:
            print("Line " + str(line_number) + " possible misspelled word: " + word) 
file.close()