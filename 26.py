"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if the given tuple list has all k elements.
'''

def check_k_elements(test_list, K):
  for tup in test_list:
    for ele in tup:
      if ele != K:
        return False
  return True

'''
Standard answer: 
def check_k_elements(test_list, K):
  res = True
  for tup in test_list:
    for ele in tup:
      if ele != K:
        res = False
  return (res) 
'''
assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True
assert check_k_elements([(7, 7, 7), (7, 7)], 7) == True
assert check_k_elements([(9, 9), (9, 9, 9, 9)], 7) == False
assert check_k_elements([(4, 4), (4, 4, 4), (4, 4), (4, 4, 6, 4), (4, )], 4) == False
