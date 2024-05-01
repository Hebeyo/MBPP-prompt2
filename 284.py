"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to check whether all items of a list are equal to a given string.
'''

def check_element(list,element):
  check_element=True
  for v in list:
    if v!=element:
      check_element=False
  return check_element

'''
Standard answer: 
def check_element(list,element):
  check_element=all(v== element for v in list)
  return check_element
'''
assert check_element(["green", "orange", "black", "white"],'blue')==False
assert check_element([1,2,3,4],7)==False
assert check_element(["green", "green", "green", "green"],'green')==True
