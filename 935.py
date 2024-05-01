"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to calculate the sum of series 1²+2²+3²+….+n².
'''

def series_sum(number):
    total = 0
    for i in range(1,number+1):
        total += i**2
    return total

'''
Standard answer: 
def series_sum(number):
 total = 0
 total = (number * (number + 1) * (2 * number + 1)) / 6
 return total
'''
assert series_sum(6)==91
assert series_sum(7)==140
assert series_sum(12)==650
