"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to find the largest prime factor of a given number.
'''

def max_Prime_Factors (n): 
    maxPrime = -1 
    while n%2 == 0: 
        maxPrime = 2
        n >>= 1    
    for i in range(3,n,2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
    if n > 2: 
        maxPrime = n  
    return int(maxPrime)

'''
Standard answer: 
import math 
def max_Prime_Factors (n): 
    maxPrime = -1 
    while n%2 == 0: 
        maxPrime = 2
        n >>= 1    
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
    if n > 2: 
        maxPrime = n  
    return int(maxPrime)
'''
assert max_Prime_Factors(15) == 5
assert max_Prime_Factors(6) == 3
assert max_Prime_Factors(2) == 2
