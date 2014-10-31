# LAB 9 - FUNCTIONS

import random

# PART 1
def minimum(x,y,z):
    """Finds minimum"""
    smallest = min(x,y,z)
    return smallest

# PART 2
def box(height, width):
    """Creates boxes of *"""
    for row in range(height):
        for column in range(width):
            print("*",end=" ")
        print()
# PART 3
def find(list, key):
    """Sorts through a list for numbers"""
    for item in range(len(list)):
        if list[item] == key:
            print("Found ", key," at position ",item)

# PART 4 -------------------------------------------
# Part 4 - Pt. 1
def create_list(list_size):
    list = []
    for i in range(list_size):
        list.append(random.randrange(1,7))
    return list

# Part 4 - Pt. 2
def count_list(list, number):
    count = 0
    for item in range(len(list)):
        if list[item] == number:
                count += 1
    return count

# Part 4 - Pt. 3
def average_list(list):
    sum = 0
    count = 0
    for item in range(len(list)):
        sum += list[item]
        count += 1
    avg = sum / count
    return int(avg)

# Part 4 - Pt. 4
my_list = create_list(10000)
for items in range(1,7):
    count = count_list(my_list,items)
    print("The number ",items," appears ",count," times in this list.")
print("The average of this list is: ",average_list(my_list))
