"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to remove all the tuples with length k.
'''

def remove_tuples(test_list, K):
  res = []
  for ele in test_list:
    if len(ele) != K:
      res.append(ele)
  return (res)

'''
Standard answer: 
def remove_tuples(test_list, K):
  res = [ele for ele in test_list if len(ele) != K]
  return (res) 
'''
assert remove_tuples([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] , 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]
assert remove_tuples([(4, 5), (4,5), (6, 7), (1, 2, 3), (3, 4, 6, 7)] ,2) == [(1, 2, 3), (3, 4, 6, 7)]
assert remove_tuples([(1, 4, 4), (4, 3), (8, 6, 7), (1, ), (3, 6, 7)] , 3) == [(4, 3), (1,)]
