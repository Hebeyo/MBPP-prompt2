"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function that matches a string that has an a followed by zero or more b's by using regex.
'''

import re
def text_match(text):
        patterns = 'ab*'
        if re.search(patterns,  text):
                return ('Found a match!')
        else:
                return ('Not matched!')

'''
Standard answer: 
import re
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return ('Found a match!')
        else:
                return ('Not matched!')
'''
assert text_match("msb") == 'Not matched!'
assert text_match("a0c") == 'Found a match!'
assert text_match("abbc") == 'Found a match!'
