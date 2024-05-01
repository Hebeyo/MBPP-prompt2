"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to find the maximum of nth column from the given tuple list.
'''

def max_of_nth(test_list, N):
  max = 0
  for i in test_list:
    if i[N] > max:
      max = i[N]
  return max

'''
Standard answer: 
def max_of_nth(test_list, N):
  res = max([sub[N] for sub in test_list])
  return (res) 
'''
assert max_of_nth([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19
assert max_of_nth([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 10
assert max_of_nth([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 1) == 11
