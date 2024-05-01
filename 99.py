"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to convert the given decimal number to its binary equivalent.
'''

def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

'''
Standard answer: 
def decimal_to_binary(n): 
    return bin(n).replace("0b","") 
'''
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(18) == '10010'
assert decimal_to_binary(7) == '111' 
