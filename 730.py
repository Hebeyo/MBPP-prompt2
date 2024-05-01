"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to remove consecutive duplicates of a given list.
'''

def consecutive_duplicates(nums):
    result=[nums[0]]
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            result.append(nums[i])
    return result

'''
Standard answer: 
from itertools import groupby
def consecutive_duplicates(nums):
    return [key for key, group in groupby(nums)] 
'''
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
assert consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[10, 15, 19, 18, 17, 26, 17, 18, 10]
assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==['a', 'b', 'c', 'd']
