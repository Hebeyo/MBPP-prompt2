"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to split a string at uppercase letters.
'''

def split_upperstring(text):
  res = []
  start = 0
  for i in range(1, len(text)):
    if text[i].isupper():
      res.append(text[start:i])
      start = i
  res.append(text[start:])
  return res

'''
Standard answer: 
import re
def split_upperstring(text):
 return (re.findall('[A-Z][^A-Z]*', text))
'''
assert split_upperstring("PythonProgramLanguage")==['Python','Program','Language']
assert split_upperstring("PythonProgram")==['Python','Program']
assert split_upperstring("ProgrammingLanguage")==['Programming','Language']
