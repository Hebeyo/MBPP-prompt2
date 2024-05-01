"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to find the sum of first even and odd number of a given list.
'''

def sum_even_odd(list1):
    first_even = -1
    first_odd = -1
    for el in list1:
        if el%2==0:
            first_even = el
            break
    for el in list1:
        if el%2!=0:
            first_odd = el
            break
    return (first_even+first_odd)

'''
Standard answer: 
def sum_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even+first_odd)
'''
assert sum_even_odd([1,3,5,7,4,1,6,8])==5
assert sum_even_odd([1,2,3,4,5,6,7,8,9,10])==3
assert sum_even_odd([1,5,7,9,10])==11
