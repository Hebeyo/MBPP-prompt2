"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to find the last digit in factorial of a given number.
'''

def last_Digit_Factorial(n):
    if n == 0:
        return 1
    elif n <= 2:
        return n
    elif n == 3:
        return 6
    elif n == 4:
        return 4
    else:
        return 0

'''
Standard answer: 
def last_Digit_Factorial(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
'''
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(21) == 0
assert last_Digit_Factorial(30) == 0
