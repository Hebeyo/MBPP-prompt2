"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to iterate over elements repeating each as many times as its count.
'''

def count_variable(a,b,c,d):
  count_a = ['p']*a
  count_b = ['q']*b
  count_c = ['r']*c
  count_d = ['s']*d
  return count_a + count_b + count_c + count_d

'''
Standard answer: 
from collections import Counter
def count_variable(a,b,c,d):
  c = Counter(p=a, q=b, r=c, s=d)
  return list(c.elements())
'''
assert count_variable(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 
assert count_variable(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 
assert count_variable(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']
