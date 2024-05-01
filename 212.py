"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of fourth power of n natural numbers.
'''

def fourth_Power_Sum(n): 
    sum = 0
    for i in range(1,n+1) : 
        sum = sum + (i*i*i*i) 
    return sum

'''
Standard answer: 
import math  
def fourth_Power_Sum(n): 
    sum = 0
    for i in range(1,n+1) : 
        sum = sum + (i*i*i*i) 
    return sum
'''
assert fourth_Power_Sum(2) == 17
assert fourth_Power_Sum(4) == 354
assert fourth_Power_Sum(6) == 2275
