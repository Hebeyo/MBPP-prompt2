"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to find the maximum element of all the given tuple records.
'''

def find_max(test_list):
  res = 0
  for i in test_list:
    for j in i:
      if int(j) > res:
        res = int(j)
  return (res)

'''
Standard answer: 
def find_max(test_list):
  res = max(int(j) for i in test_list for j in i)
  return (res) 
'''
assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
assert find_max([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
assert find_max([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12
