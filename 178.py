"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to search some literals strings in a string.
'''

def string_literals(patterns,text):
  for pattern in patterns:
     if pattern in text:
       return ('Matched!')
  return ('Not Matched!')

'''
Standard answer: 
import re
def string_literals(patterns,text):
  for pattern in patterns:
     if re.search(pattern,  text):
       return ('Matched!')
     else:
       return ('Not Matched!')
'''
assert string_literals(['language'],'python language')==('Matched!')
assert string_literals(['program'],'python language')==('Not Matched!')
assert string_literals(['python'],'programming language')==('Not Matched!')
