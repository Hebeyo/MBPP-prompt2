"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to count repeated items of a tuple.
'''

def count_tuplex(tuplex, value):
  count = 0
  for i in tuplex:
    if i == value:
      count += 1
  return count

'''
Standard answer: 
def count_tuplex(tuplex,value):  
  count = tuplex.count(value)
  return count
'''
assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),4)==3
assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),2)==2
assert count_tuplex((2, 4, 7, 7, 7, 3, 4, 4, 7),7)==4
