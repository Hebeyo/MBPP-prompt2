"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to group a sequence of key-value pairs into a dictionary of lists.
'''

def group_keyvalue(l):
    result = {}
    for k, v in l:
        if k in result:
            result[k].append(v)
        else:
            result[k] = [v]
    return result

'''
Standard answer: 
def group_keyvalue(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
'''
assert group_keyvalue([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])=={'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
assert group_keyvalue([('python', 1), ('python', 2), ('python', 3), ('python', 4), ('python', 5)])=={'python': [1,2,3,4,5]}
assert group_keyvalue([('yellow',100), ('blue', 200), ('yellow', 300), ('blue', 400), ('red', 100)])=={'yellow': [100, 300], 'blue': [200, 400], 'red': [100]}
