"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""


'''Write a function to find the equilibrium index of the given array.
'''
def equilibrium_index(arr):
  for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
      return i
  return -1

'''
Standard answer: 
def equilibrium_index(arr):
  total_sum = sum(arr)
  left_sum=0
  for i, num in enumerate(arr):
    total_sum -= num
    if left_sum == total_sum:
      return i
    left_sum += num
  return -1
'''
assert equilibrium_index([1, 2, 3, 4, 1, 2, 3]) == 3
assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3
assert equilibrium_index([1, 2, 3]) == -1
