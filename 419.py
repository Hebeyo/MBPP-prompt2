"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
'''

def round_and_sum(list1):
  round_and_sum = 0
  for i in list1:
    round_and_sum += round(i)
  return round_and_sum * len(list1)

'''
Standard answer: 
def round_and_sum(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum
'''
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
assert round_and_sum([5,2,9,24.3,29])==345
assert round_and_sum([25.0,56.7,89.2])==513
