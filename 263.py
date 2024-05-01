"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to merge two dictionaries.
'''

def merge_dict(d1,d2):
 d = d1.copy()
 d.update(d2)
 return d

'''
Standard answer: 
def merge_dict(d1,d2):
 d = d1.copy()
 d.update(d2)
 return d
'''
assert merge_dict({'a': 100, 'b': 200},{'x': 300, 'y': 200})=={'x': 300, 'y': 200, 'a': 100, 'b': 200}
assert merge_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})=={'a':900,'b':900,'d':900,'a':900,'b':900,'d':900}
assert merge_dict({'a':10,'b':20},{'x':30,'y':40})=={'x':30,'y':40,'a':10,'b':20}
