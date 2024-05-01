"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a python function to find the sum of even factors of a number.
'''

def sumofFactors(n):
    result = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            result += i
    return result

'''
Standard answer: 
import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res 
'''
assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8
