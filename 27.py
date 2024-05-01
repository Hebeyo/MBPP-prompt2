"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a python function to remove all digits from a list of strings.
'''

def remove(list):
    new_list = []
    for i in list:
        new_list.append(''.join([j for j in i if not j.isdigit()]))
    return new_list
'''
Standard answer: 
import re  
def remove(list): 
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list] 
    return list
'''
assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
assert remove(['28Jan','12Jan','11Jan']) == ['Jan','Jan','Jan']
assert remove(['wonder1','wonder2','wonder3']) == ['wonder','wonder','wonder']
