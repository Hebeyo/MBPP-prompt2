"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the n'th perrin number using recursion.
'''

def get_perrin(n):
  if n == 0:
    return 3
  if n == 1:
    return 0
  if n == 2:
    return 2
  return get_perrin(n - 2) + get_perrin(n - 3)

'''
Standard answer: 
def get_perrin(n):
  if (n == 0):
    return 3
  if (n == 1):
    return 0
  if (n == 2):
    return 2 
  return get_perrin(n - 2) + get_perrin(n - 3)
'''
assert get_perrin(9) == 12
assert get_perrin(4) == 2
assert get_perrin(6) == 5
