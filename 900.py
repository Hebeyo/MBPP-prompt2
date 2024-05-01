"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function where a string will start with a specific number.
'''

def match_num(string):
    if string[0]=='5':
        return True
    else:
        return False

'''
Standard answer: 
import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
'''
assert match_num('5-2345861')==True
assert match_num('6-2345861')==False
assert match_num('78910')==False
