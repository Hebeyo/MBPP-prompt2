"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a python function to find the sum of squares of binomial co-efficients.
'''

def sum_of_square(n):
    def factorial(start,end): 
        res = 1 
        for i in range(start,end + 1): 
            res *= i      
        return res
    return int(factorial(n + 1, 2 * n)  /factorial(1, n))

'''
Standard answer: 
def factorial(start,end): 
    res = 1 
    for i in range(start,end + 1): 
        res *= i      
    return res 
def sum_of_square(n): 
   return int(factorial(n + 1, 2 * n)  /factorial(1, n)) 
'''
assert sum_of_square(4) == 70
assert sum_of_square(5) == 252
assert sum_of_square(2) == 6
