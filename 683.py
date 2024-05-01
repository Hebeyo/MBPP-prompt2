"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether the given number can be represented by sum of two squares or not.
'''

def sum_Square(n) : 
    for i in range(1, int(n ** 0.5) + 1) : 
        for j in range(1, int(n ** 0.5) + 1) : 
            if (i * i + j * j == n) : 
                return True
    return False
'''
Standard answer: 
def sum_Square(n) : 
    i = 1 
    while i*i <= n : 
        j = 1
        while (j*j <= n) : 
            if (i*i+j*j == n) : 
                return True
            j = j+1
        i = i+1     
    return False
'''
assert sum_Square(25) == True
assert sum_Square(24) == False
assert sum_Square(17) == True
