"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to find tuples which have all elements divisible by k from the given list of tuples.
'''

def find_tuples(test_list, K):
  res = []
  for sub in test_list:
    if all(ele % K == 0 for ele in sub):
      res.append(sub)
  return (str(res))

'''
Standard answer: 
def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return (str(res)) 
'''
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == '[(6, 24, 12)]'
assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == '[(5, 25, 30)]'
assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == '[(8, 16, 4)]'
