"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to add consecutive numbers of a given list.
'''

def add_consecutive_nums(nums):
    return [nums[i]+nums[i+1] for i in range(len(nums)-1)]

'''
Standard answer: 
def add_consecutive_nums(nums):
    result = [b+a for a, b in zip(nums[:-1], nums[1:])]
    return result
'''
assert add_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[2, 4, 7, 8, 9, 11, 13]
assert add_consecutive_nums([4, 5, 8, 9, 6, 10])==[9, 13, 17, 15, 16]
assert add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[3, 5, 7, 9, 11, 13, 15, 17, 19]
