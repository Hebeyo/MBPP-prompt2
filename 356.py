"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the third angle of a triangle using two angles.
'''

def find_angle(a,b):
 c = 180 - (a + b)
 return c

'''
Standard answer: 
def find_angle(a,b):
 c = 180 - (a + b)
 return c

'''
assert find_angle(47,89)==44
assert find_angle(45,95)==40
assert find_angle(50,40)==90
