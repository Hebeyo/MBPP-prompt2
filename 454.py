"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function that matches a word containing 'z'.
'''

def text_match_wordz(text):
    import re
    patterns = '\w*z.\w*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

'''
Standard answer: 
import re
def text_match_wordz(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_wordz("pythonz.")==('Found a match!')
assert text_match_wordz("xyz.")==('Found a match!')
assert text_match_wordz("  lang  .")==('Not matched!')
