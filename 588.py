"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a python function to find the difference between largest and smallest value in a given array.
'''

def big_diff(nums):
    min = nums[0]
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]
    return max - min

'''
Standard answer: 
def big_diff(nums):
     diff= max(nums)-min(nums)
     return diff
'''
assert big_diff([1,2,3,4]) == 3
assert big_diff([4,5,12]) == 8
assert big_diff([9,2,3]) == 7
