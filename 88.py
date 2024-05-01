"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to get the frequency of the elements in a list.
'''

def freq_count(list1):
  freq_count= {}
  for i in list1:
    if i in freq_count:
      freq_count[i] += 1
    else:
      freq_count[i] = 1
  return freq_count

'''
Standard answer: 
import collections
def freq_count(list1):
  freq_count= collections.Counter(list1)
  return freq_count
'''
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1}) 
assert freq_count([1,2,3,4,3,2,4,1,3,1,4])==({1:3, 2:2,3:3,4:3}) 
assert freq_count([5,6,7,4,9,10,4,5,6,7,9,5])==({10:1,5:3,6:2,7:2,4:2,9:2}) 
