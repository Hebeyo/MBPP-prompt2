"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to extract a specified column from a given nested list.
'''

def extract_column(list1, n):
   result = []
   for i in list1:
      result.append(i.pop(n))
   return result

'''
Standard answer: 
def extract_column(list1, n):
   result = [i.pop(n) for i in list1]
   return result 
'''
assert extract_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[1, 2, 1]
assert extract_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[3, -5, 1]
assert extract_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[1, 5, 1, 13, 5, 9]
