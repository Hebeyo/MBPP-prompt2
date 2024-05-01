"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether the product of numbers is even or not.
'''

def is_Product_Even(arr,n): 
    even = 0
    for i in range(0,n): 
        if ((arr[i] & 1) == 0): 
            return True
    return False

'''
Standard answer: 
def is_Product_Even(arr,n): 
    for i in range(0,n): 
        if ((arr[i] & 1) == 0): 
            return True
    return False
'''
assert is_Product_Even([1,2,3],3) == True
assert is_Product_Even([1,2,1,4],4) == True
assert is_Product_Even([1,1],2) == False
