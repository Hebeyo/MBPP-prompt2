"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count positive numbers in a list.
'''

def pos_count(list):
  pos_count = 0
  for num in list:
    if num > 0:
      pos_count += 1
  return pos_count

'''
Standard answer: 
def pos_count(list):
  pos_count= 0
  for num in list: 
    if num >= 0: 
      pos_count += 1
  return pos_count 
'''
assert pos_count([1,-2,3,-4]) == 2
assert pos_count([3,4,5,-1]) == 3
assert pos_count([1,2,3,4]) == 4
