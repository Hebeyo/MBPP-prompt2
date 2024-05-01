"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to count the most common character in a given string.
'''

def max_char(str1):
    max_count = 0
    max_char = ''
    for i in set(str1):
        if str1.count(i) > max_count:
            max_count = str1.count(i)
            max_char = i
    return max_char

'''
Standard answer: 
from collections import Counter 
def max_char(str1):
    temp = Counter(str1) 
    max_char = max(temp, key = temp.get)
    return max_char
'''
assert max_char("hello world")==('l')
assert max_char("hello ")==('l')
assert max_char("python pr")==('p')
