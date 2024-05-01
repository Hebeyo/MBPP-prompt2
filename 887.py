"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether the given number is odd or not using bitwise operator.
'''

def is_odd(n) : 
    if (n & 1) :
        return True; 
    else :
        return False;

'''
Standard answer: 
def is_odd(n) : 
    if (n^1 == n-1) :
        return True; 
    else :
        return False; 
'''
assert is_odd(5) == True
assert is_odd(6) == False
assert is_odd(7) == True
