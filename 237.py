"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to check the occurrences of records which occur similar times in the given tuples.
'''

def check_occurences(test_list):
  res = {}
  for i in test_list:
    if tuple(sorted(i)) in res:
      res[tuple(sorted(i))] += 1
    else:
      res[tuple(sorted(i))] = 1
  return res


'''
Standard answer: 
from collections import Counter 
def check_occurences(test_list):
  res = dict(Counter(tuple(ele) for ele in map(sorted, test_list)))
  return  (res) 
'''
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
assert check_occurences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
assert check_occurences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}
