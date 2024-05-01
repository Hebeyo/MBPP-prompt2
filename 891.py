"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether the given two numbers have same number of digits or not.
'''

def same_Length(A,B): 
    A = str(A)
    B = str(B)
    if len(A) == len(B):
        return True
    return False

'''
Standard answer: 
def same_Length(A,B): 
    while (A > 0 and B > 0): 
        A = A / 10; 
        B = B / 10; 
    if (A == 0 and B == 0): 
        return True; 
    return False; 
'''
assert same_Length(12,1) == False
assert same_Length(2,2) == True
assert same_Length(10,20) == True
