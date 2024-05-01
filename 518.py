"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to find the square root of a perfect number.
'''

def sqrt_root(num):
    sqrt_root = num ** 0.5
    return sqrt_root

'''
Standard answer: 
import math
def sqrt_root(num):
 sqrt_root = math.pow(num, 0.5)
 return sqrt_root 
'''
assert sqrt_root(4)==2
assert sqrt_root(16)==4
assert sqrt_root(400)==20
