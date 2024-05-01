"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to extract specified number of elements from a given list, which follow each other continuously.
'''

def extract_elements(numbers, n):
    i = 0
    result = []
    while i < len(numbers):
        if numbers[i:i+n] == [numbers[i]]*n:
            result.append(numbers[i])
        i += 1
    return result

'''
Standard answer: 
from itertools import groupby 
def extract_elements(numbers, n):
    result = [i for i, j in groupby(numbers) if len(list(j)) == n] 
    return result
'''
assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]
assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]
assert extract_elements([0,0,0,0,0],5)==[0]
