"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether two given lines are parallel or not.
'''

def parallel_lines(line1, line2):
    return (line1[0]/line1[1]) == (line2[0]/line2[1])

'''
Standard answer: 
def parallel_lines(line1, line2):
  return line1[0]/line1[1] == line2[0]/line2[1]
'''
assert parallel_lines([2,3,4], [2,3,8]) == True
assert parallel_lines([2,3,4], [4,-3,8]) == False
assert parallel_lines([3,3],[5,5]) == True
