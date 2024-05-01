"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to reflect the run-length encoding from a list.
'''

def encode_list(list1):
    encoded_list=[]
    i=0
    while i<len(list1):
        count=1
        while i+1<len(list1) and list1[i]==list1[i+1]:
            i+=1
            count+=1
        encoded_list.append([count,list1[i]])
        i+=1
    return encoded_list

'''
Standard answer: 
from itertools import groupby
def encode_list(list1):
    return [[len(list(group)), key] for key, group in groupby(list1)]
'''
assert encode_list([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
assert encode_list('automatically')==[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
assert encode_list('python')==[[1, 'p'], [1, 'y'], [1, 't'], [1, 'h'], [1, 'o'], [1, 'n']]
