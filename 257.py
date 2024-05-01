"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to swap two numbers.
'''

def swap_numbers(a,b):
 temp = a
 a = b
 b = temp
 return (a,b)

'''
Standard answer: 
def swap_numbers(a,b):
 temp = a
 a = b
 b = temp
 return (a,b)
'''
assert swap_numbers(10,20)==(20,10)
assert swap_numbers(15,17)==(17,15)
assert swap_numbers(100,200)==(200,100)
