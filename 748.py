"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to put spaces between words starting with capital letters in a given string by using regex.
'''

import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

'''
Standard answer: 
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
'''
assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'
