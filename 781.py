"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether the count of divisors is even or odd.
'''

def count_Divisors(n) : 
    count = 0
    for i in range(1, n + 1) : 
        if (n % i == 0) : 
            count = count + 1
    if (count % 2 == 0) : 
        return ("Even") 
    else : 
        return ("Odd")

'''
Standard answer: 
import math 
def count_Divisors(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    if (count % 2 == 0) : 
        return ("Even") 
    else : 
        return ("Odd") 
'''
assert count_Divisors(10) == "Even"
assert count_Divisors(100) == "Odd"
assert count_Divisors(125) == "Even"
