"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to count the same pair in two given lists using map function.
'''

from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result

'''
Standard answer: 
from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result
'''
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
assert count_same_pair([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==11
assert count_same_pair([2, 4, -6, -9, 11, -12, 14, -5, 17],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==1
