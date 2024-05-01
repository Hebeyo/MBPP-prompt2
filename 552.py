"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to check whether a given sequence is linear or not.
'''

def Seq_Linear(seq_nums):
  for i in range(1, len(seq_nums)):
    if seq_nums[i] - seq_nums[i-1] != seq_nums[1] - seq_nums[0]:
      return "Non Linear Sequence"
  return "Linear Sequence"
'''
Standard answer: 
def Seq_Linear(seq_nums):
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: 
    return "Linear Sequence"
  else:
    return "Non Linear Sequence"
'''
assert Seq_Linear([0,2,4,6,8,10]) == "Linear Sequence"
assert Seq_Linear([1,2,3]) == "Linear Sequence"
assert Seq_Linear([1,5,2]) == "Non Linear Sequence"
