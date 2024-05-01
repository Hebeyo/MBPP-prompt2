"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to check if all the elements in tuple have same data type or not.
'''

def check_type(test_tuple):
  return len(set(map(type, test_tuple))) == 1

'''
Standard answer: 
def check_type(test_tuple):
  res = True
  for ele in test_tuple:
    if not isinstance(ele, type(test_tuple[0])):
      res = False
      break
  return (res) 
'''
assert check_type((5, 6, 7, 3, 5, 6) ) == True
assert check_type((1, 2, "4") ) == False
assert check_type((3, 2, 1, 4, 5) ) == True
