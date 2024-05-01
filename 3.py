"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to identify non-prime numbers.
'''

def is_not_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return True
    return False


'''
Standard answer: 
import math
def is_not_prime(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
'''
assert is_not_prime(2) == False
assert is_not_prime(10) == True
assert is_not_prime(35) == True
