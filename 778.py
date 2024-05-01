"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to pack consecutive duplicates of a given list elements into sublists.
'''

def pack_consecutive_duplicates(list1):
    res = []
    for i in range(len(list1)):
        if i == 0 or list1[i] != list1[i-1]:
            res.append([list1[i]])
        else:
            res[-1].append(list1[i])
    return res

'''
Standard answer: 
from itertools import groupby
def pack_consecutive_duplicates(list1):
    return [list(group) for key, group in groupby(list1)]
'''
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]
