"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to sort a list in a dictionary.
'''

def sorted_dict(dict1):
  sorted_dict = {x: sorted(dict1[x]) for x in dict1}
  return sorted_dict

'''
Standard answer: 
def sorted_dict(dict1):
  sorted_dict = {x: sorted(y) for x, y in dict1.items()}
  return sorted_dict
'''
assert sorted_dict({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]})=={'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
assert sorted_dict({'n1': [25,37,41], 'n2': [41,54,63], 'n3': [29,38,93]})=={'n1': [25, 37, 41], 'n2': [41, 54, 63], 'n3': [29, 38, 93]}
assert sorted_dict({'n1': [58,44,56], 'n2': [91,34,58], 'n3': [100,200,300]})=={'n1': [44, 56, 58], 'n2': [34, 58, 91], 'n3': [100, 200, 300]}
