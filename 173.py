"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to remove everything except alphanumeric characters from a string.
'''

def remove_splchar(text):
    return ''.join(e for e in text if e.isalnum())

'''
Standard answer: 
import re
def remove_splchar(text): 
 pattern = re.compile('[\W_]+')
 return (pattern.sub('', text))
'''
assert remove_splchar('python  @#&^%$*program123')==('pythonprogram123')
assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')
assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program')==('python67program')
