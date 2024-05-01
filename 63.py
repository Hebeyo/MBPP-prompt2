"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the maximum difference between available pairs in the given tuple list.
'''

def max_difference(test_list):
  temp = []
  for a, b in test_list:
    temp.append(abs(b - a))
  res = max(temp)
  return res

'''
Standard answer: 
def max_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = max(temp)
  return (res) 
'''
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
