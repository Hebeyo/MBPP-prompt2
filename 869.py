"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""


'''Write a function to remove sublists from a given list of lists, which are outside a given range.
'''

def remove_list_range(list1, leftrange, rigthrange):
    res = []
    for i in list1:
        if min(i)>=leftrange and max(i)<=rigthrange:
            res.append(i)
    return res

'''
Standard answer: 
def remove_list_range(list1, leftrange, rigthrange):
   result = [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]
   return result
'''
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],13,17)==[[13, 14, 15, 17]]
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],1,3)==[[2], [1, 2, 3]]
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]
