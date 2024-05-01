"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to get a colon of a tuple.
'''

def colon_tuplex(tuplex,m,n):
  tuplex_colon = list(tuplex)
  tuplex_colon[m].append(n)
  return tuple(tuplex_colon)

'''
Standard answer: 
from copy import deepcopy
def colon_tuplex(tuplex,m,n):
  tuplex_colon = deepcopy(tuplex)
  tuplex_colon[m].append(n)
  return tuplex_colon
'''
assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 
assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)
