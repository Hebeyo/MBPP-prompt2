"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to find the largest triangle that can be inscribed in an ellipse.
'''

import math
def largest_triangle(a,b): 
    if (a < 0 or b < 0): 
        return -1 
    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  
    return area


'''
Standard answer: 
import math
def largest_triangle(a,b): 
    if (a < 0 or b < 0): 
        return -1 
    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  
    return area 
'''
assert largest_triangle(4,2)==10.392304845413264
assert largest_triangle(5,7)==4.639421805988064
assert largest_triangle(9,1)==105.2220865598093
