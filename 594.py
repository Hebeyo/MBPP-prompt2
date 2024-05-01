"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to find the difference of first even and odd number of a given list.
'''

def diff_even_odd(list1):
    first_even = -1
    first_odd = -1
    for i in range(len(list1)):
        if list1[i]%2==0:
            first_even = list1[i]
            break
    for i in range(len(list1)):
        if list1[i]%2!=0:
            first_odd = list1[i]
            break
    return (first_even-first_odd)

'''
Standard answer: 
def diff_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
'''
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
assert diff_even_odd([1,5,7,9,10])==9
