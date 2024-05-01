"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to check if each element of second tuple is smaller than its corresponding index in first tuple.
'''

def check_smaller(test_tup1, test_tup2):
  res = True
  for i in range(len(test_tup1)):
    if test_tup1[i] <= test_tup2[i]:
      res = False
  return res

'''
Standard answer: 
def check_smaller(test_tup1, test_tup2):
  res = all(x > y for x, y in zip(test_tup1, test_tup2))
  return (res) 
'''
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((4, 5, 6), (3, 4, 5)) == True
assert check_smaller((11, 12, 13), (10, 11, 12)) == True
