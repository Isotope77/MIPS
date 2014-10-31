# LAB 9 - FUNCTIONS

import random

# Part 1 - Minimum
def minimum(x,y,z):
    smallest = min(x,y,z)
    return smallest

# Part 2 - Box
def box(height, width):
    for row in range(height):
        for column in range(width):
            print("*",end=" ")
        print()
# Part 3
def find(list, key):
    for item in range(len(list)):
        if list[item] == key:
            print("Found ", key," at position ",item)

# Part 4 - Pt. 1
def create_list(list_size):
    list = []
    for i in range(list_size):
        list.append(random.randrange(6))
    return list
my_list = create_list(5)
print(my_list)