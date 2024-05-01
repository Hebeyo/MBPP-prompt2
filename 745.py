"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to find numbers within a given range where every number is divisible by every digit it contains.
'''

def divisible_by_digits(startnum, endnum):
    res = []
    for n in range(startnum, endnum+1):
        if all([int(x) != 0 and n%int(x) == 0 for x in str(n)]):
            res.append(n)
    return res

'''
Standard answer: 
def divisible_by_digits(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
'''
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
assert divisible_by_digits(20,25)==[22, 24]
