"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to convert the given string of float type into tuple.
'''

def float_to_tuple(test_str):
  res = tuple(map(float, test_str.split(', ')))
  return (res)

'''
Standard answer: 
def float_to_tuple(test_str):
  res = tuple(map(float, test_str.split(', ')))
  return (res) 
'''
assert float_to_tuple("1.2, 1.3, 2.3, 2.4, 6.5") == (1.2, 1.3, 2.3, 2.4, 6.5)
assert float_to_tuple("2.3, 2.4, 5.6, 5.4, 8.9") == (2.3, 2.4, 5.6, 5.4, 8.9)
assert float_to_tuple("0.3, 0.5, 7.8, 9.4") == (0.3, 0.5, 7.8, 9.4)
