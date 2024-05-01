"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""


'''Write a function to find the first duplicate element in a given array of integers.
'''

def find_first_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return -1

'''
Standard answer: 
def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate
'''
assert find_first_duplicate(([1, 2, 3, 4, 4, 5]))==4
assert find_first_duplicate([1, 2, 3, 4])==-1
assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2])==1
