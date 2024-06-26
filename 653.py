"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to group a sequence of key-value pairs into a dictionary of lists using collections module.
'''

from collections import defaultdict
def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d

'''
Standard answer: 
from collections import defaultdict
def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d
'''
assert grouping_dictionary([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])== ({'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
assert grouping_dictionary([('yellow', 10), ('blue', 20), ('yellow', 30), ('blue', 40), ('red', 10)])== ({'yellow': [10, 30], 'blue': [20, 40], 'red': [10]})
assert grouping_dictionary([('yellow', 15), ('blue', 25), ('yellow', 35), ('blue', 45), ('red', 15)])== ({'yellow': [15, 35], 'blue': [25, 45], 'red': [15]})
