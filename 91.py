"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to check if a substring is present in a given list of string values.
'''

def find_substring(str1, sub_str):
  for s in str1:
    if sub_str in s:
      return True
  return False

'''
Standard answer: 
def find_substring(str1, sub_str):
   if any(sub_str in s for s in str1):
       return True
   return False
'''
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True
