"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if the given tuples contain the k or not.
'''

def check_K(test_tup, K):
  return K in test_tup

'''
Standard answer: 
def check_K(test_tup, K):
  res = False
  for ele in test_tup:
    if ele == K:
      res = True
      break
  return (res) 
'''
assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((1, 2, 3, 4, 5, 6), 7) == False
assert check_K((7, 8, 9, 44, 11, 12), 11) == True
