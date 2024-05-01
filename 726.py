"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to multiply the adjacent elements of the given tuple.
'''

def multiply_elements(test_tup):
  res = []
  for i in range(len(test_tup)-1):
    res.append(test_tup[i] * test_tup[i+1])
  return tuple(res)


'''
Standard answer: 
def multiply_elements(test_tup):
  res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 
'''
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
