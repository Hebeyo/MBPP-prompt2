"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""


'''Write a python function to check whether the two numbers differ at one bit position only or not.
'''

def differ_At_One_Bit_Pos(a,b):
    count = 0
    while a or b:
        if a & 1 != b & 1:
            count += 1
        a >>= 1
        b >>= 1
    return count == 1


'''
Standard answer: 
def is_Power_Of_Two (x): 
    return x and (not(x & (x - 1))) 
def differ_At_One_Bit_Pos(a,b): 
    return is_Power_Of_Two(a ^ b)
'''
assert differ_At_One_Bit_Pos(13,9) == True
assert differ_At_One_Bit_Pos(15,8) == False
assert differ_At_One_Bit_Pos(2,4) == False
