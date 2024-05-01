"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the last digit of a given number.
'''

def last_Digit(n) :
    return (n % 10)

'''
Standard answer: 
def last_Digit(n) :
    return (n % 10) 
'''
assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0
