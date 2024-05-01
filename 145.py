"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to find the maximum difference between any two elements in a given array.
'''

def max_Abs_Diff(arr,n):
  minEle = arr[0] 
  maxEle = arr[0] 
  for i in range(1, n): 
    minEle = min(minEle,arr[i]) 
    maxEle = max(maxEle,arr[i]) 
  return (maxEle - minEle)

'''
Standard answer: 
def max_Abs_Diff(arr,n): 
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
'''
assert max_Abs_Diff((2,1,5,3),4) == 4
assert max_Abs_Diff((9,3,2,5,1),5) == 8
assert max_Abs_Diff((3,2,1),3) == 2
