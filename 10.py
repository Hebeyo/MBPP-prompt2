"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to get the n smallest items from a dataset.
'''

import heapq
def small_nnum(list1,n):
  smallest=heapq.nsmallest(n,list1)
  return smallest

'''
Standard answer: 
import heapq
def small_nnum(list1,n):
  smallest=heapq.nsmallest(n,list1)
  return smallest
'''
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20]
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[10,20,20,40,50]
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[10,20,20]
