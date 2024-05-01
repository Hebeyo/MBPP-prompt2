"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to check whether the given string is starting with a vowel or not using regex.
'''

import re
def check_str(string):
    pattern = '^[aeiouAEIOU][A-Za-z0-9_]*'
    if re.match(pattern, string):
        return 'Valid'
    else:
        return 'Invalid'

'''
Standard answer: 
import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	if(re.search(regex, string)): 
		return ("Valid") 
	else: 
		return ("Invalid") 
'''
assert check_str("annie") == 'Valid'
assert check_str("dawood") == 'Invalid'
assert check_str("Else") == 'Valid'
