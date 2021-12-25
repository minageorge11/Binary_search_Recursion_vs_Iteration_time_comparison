'''This code represents a comparison in time between binary search with recursion and normal search in a set of 10,000 integer. 
The operation is repeated to search for every integer in the 10,000 integers. 
The time is logged and the total time is represented for comparison.'''


import random
import time


def normal_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return True

bottom = 1
top = 10000
midpoint = 5000

def Binary_search(list, target, bottom, top, midpoint):
    # If the midpoint of the search range equals the target, the operation ends successfully.
    if list[midpoint - 1] == target: return True
    
    # If the midpoint is more than the target, drop down the top of the search range to the midpoint, and call the function again with new range. 
    elif list[midpoint - 1] > target:
        new_top = midpoint
        new_bottom = bottom
        new_midpoint = (new_top + new_bottom) // 2
        return Binary_search(list, target, new_bottom, new_top, new_midpoint)
        
    # If the midpoint is less than the target, raise the bottom of the search range to the midpoint, and call the function again with new range.
    elif list[midpoint - 1] < target:
        new_bottom = midpoint
        new_top = top
        new_midpoint = -(-(new_top + new_bottom) // 2)
        return Binary_search(list, target, new_bottom, new_top, new_midpoint)

# Created a set of 10000 integer.
list = set()
while len(list) < 10000:
    list.add(random.randint(-10000, 10000))

list = sorted(list)


# Run normal search for every integer in the set and log the time
start_time = time.time()
for target in list:
    normal_search(list, target)
end_time = time.time()
print("Complete duration for normal search is: ", (end_time - start_time))


# Run Binary search for every integer in the set and log the time
start_time = time.time()
for target in list:
    Binary_search(list, target, 1, 10000, 5000)
end_time = time.time()
print("Complete duration for Binary search is: ", (end_time - start_time))
