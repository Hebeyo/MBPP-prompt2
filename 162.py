"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
'''

def sum_series(n):
  result = 0
  while n > 0:
    result += n
    n -= 2
  return result

'''
Standard answer: 
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)
'''
assert sum_series(6)==12
assert sum_series(10)==30
assert sum_series(9)==25
