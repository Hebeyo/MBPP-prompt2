"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to find t-nth term of arithemetic progression.
'''

def tn_ap(a,n,d):
  tn = a
  for i in range(n-1):
    tn += d
  return tn

'''
Standard answer: 
def tn_ap(a,n,d):
  tn = a + (n - 1) * d
  return tn
'''
assert tn_ap(1,5,2)==9
assert tn_ap(2,6,4)==22
assert tn_ap(1,4,5)==16
