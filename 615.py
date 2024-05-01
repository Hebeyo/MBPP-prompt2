"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to find average value of the numbers in a given tuple of tuples.
'''

def average_tuple(nums):
    result = []
    for i in range(len(nums[0])):
        sum = 0
        for j in range(len(nums)):
            sum += nums[j][i]
        result.append(sum/len(nums))
    return result

'''
Standard answer: 
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result
'''
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
assert average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)))== [25.5, -18.0, 3.75]
assert average_tuple( ((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40)))==[305.0, 342.5, 270.0, 232.5]
