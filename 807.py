"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""


'''Write a python function to find the first odd number in a given list of numbers.
'''

def first_odd(nums):
    for i in range(len(nums)):
        if nums[i]%2!=0:
            return nums[i]
    return -1

'''
Standard answer: 
def first_odd(nums):
  first_odd = next((el for el in nums if el%2!=0),-1)
  return first_odd
'''
assert first_odd([1,3,5]) == 1
assert first_odd([2,4,1,3]) == 1
assert first_odd ([8,9,1]) == 9
