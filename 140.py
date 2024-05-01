"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to extract elements that occur singly in the given tuple list.
'''

def extract_singly(test_list):
  res = []
  temp = set()
  for inner in test_list:
    for ele in inner:
      if not ele in temp:
        temp.add(ele)
        res.append(ele)
  return (res)

'''
Standard answer: 
def extract_singly(test_list):
  res = []
  temp = set()
  for inner in test_list:
    for ele in inner:
      if not ele in temp:
        temp.add(ele)
        res.append(ele)
  return (res) 
'''
assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]
assert extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)]) == [1, 2, 3, 4, 7, 8]
assert extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)]) == [7, 8, 9, 10, 11, 12]
