"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to sum elements in two lists.
'''

def sum_list(lst1,lst2):
  res_list = []
  for i in range(len(lst1)):
    res_list.append(lst1[i] + lst2[i])
  return res_list

'''
Standard answer: 
def sum_list(lst1,lst2):
  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 
  return res_list
'''
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
assert sum_list([1,2,3],[5,6,7])==[6,8,10]
assert sum_list([15,20,30],[15,45,75])==[30,65,105]
