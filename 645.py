"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to find the product of it’s kth index in the given tuples.
'''

def find_k_product(test_list, K):
  res = 1
  for i in range(len(test_list)):
    res *= test_list[i][K]
  return (res)

'''
Standard answer: 
def get_product(val) : 
	res = 1
	for ele in val: 
		res *= ele 
	return res 
def find_k_product(test_list, K):
  res = get_product([sub[K] for sub in test_list])
  return (res) 
'''
assert find_k_product([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 665
assert find_k_product([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 280
assert find_k_product([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 0) == 210
