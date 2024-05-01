"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function that matches a string that has an a followed by three 'b'.
'''

def text_match_three(text):
        import re
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

'''
Standard answer: 
import re
def text_match_three(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_three("ac")==('Not matched!')
assert text_match_three("dc")==('Not matched!')
assert text_match_three("abbbba")==('Found a match!')
