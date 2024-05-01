"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to zip two given lists of lists.
'''

def zip_list(list1,list2):
  result = []
  for x,y in zip(list1,list2):
    result.append(x+y)
  return result

'''
Standard answer: 
def zip_list(list1,list2):  
 result = list(map(list.__add__, list1, list2)) 
 return result
'''
assert zip_list([[1, 3], [5, 7], [9, 11]] ,[[2, 4], [6, 8], [10, 12, 14]] )==[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
assert zip_list([[1, 2], [3, 4], [5, 6]] ,[[7, 8], [9, 10], [11, 12]] )==[[1, 2, 7, 8], [3, 4, 9, 10], [5, 6, 11, 12]]
assert zip_list([['a','b'],['c','d']] , [['e','f'],['g','h']] )==[['a','b','e','f'],['c','d','g','h']]
