"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to get the sum of a non-negative integer.
'''

def sum_digits(n):
  return sum(int(i) for i in str(n))

'''
Standard answer: 
def sum_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))
'''
assert sum_digits(345)==12
assert sum_digits(12)==3
assert sum_digits(97)==16
