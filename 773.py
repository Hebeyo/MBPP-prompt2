"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to find the occurrence and position of the substrings within a string.
'''

def occurance_substring(text,pattern):
  for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)]==pattern:
      return (pattern, i, i+len(pattern))
  return None

'''
Standard answer: 
import re
def occurance_substring(text,pattern):
 for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    return (text[s:e], s, e)
'''
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
