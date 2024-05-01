"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function that matches a string that has an a followed by one or more b's.
'''

def text_match_one(text):
    if text[0]=='a' and text[1]=='b':
        return 'Found a match!'
    else:
        return('Not matched!')

'''
Standard answer: 
import re
def text_match_one(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

'''
assert text_match_one("ac")==('Not matched!')
assert text_match_one("dc")==('Not matched!')
assert text_match_one("abba")==('Found a match!')
