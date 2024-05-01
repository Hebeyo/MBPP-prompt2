"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to find the previous palindrome of a specified number.
'''

def previous_palindrome(num):
    for i in range(num-1,0,-1):
        if str(i) == str(i)[::-1]:
            return i
    return -1

'''
Standard answer: 
def previous_palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
'''
assert previous_palindrome(99)==88
assert previous_palindrome(1221)==1111
assert previous_palindrome(120)==111
