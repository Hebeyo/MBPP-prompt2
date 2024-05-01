"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to check whether the given month number contains 30 days or not.
'''

def check_monthnumber_number(monthnum3):
  if monthnum3 in [4, 6, 9, 11]:
    return True
  else:
    return False

'''
Standard answer: 
def check_monthnumber_number(monthnum3):
  if(monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11):
    return True
  else:
    return False
'''
assert check_monthnumber_number(6)==True
assert check_monthnumber_number(2)==False
assert check_monthnumber_number(12)==False
