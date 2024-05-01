"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to replace multiple occurence of character by single.
'''

def replace(string, char):
    while char*2 in string:
        string = string.replace(char*2, char)
    return string

'''
Standard answer: 
import re 
def replace(string, char): 
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string 
'''
assert replace('peep','e') == 'pep'
assert replace('Greek','e') == 'Grek'
assert replace('Moon','o') == 'Mon'
