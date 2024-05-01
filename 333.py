"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a python function to sort a list according to the second element in sublist.
'''

def Sort(sub_li): 
    n = len(sub_li) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if sub_li[j][1] > sub_li[j+1][1] : 
                sub_li[j], sub_li[j+1] = sub_li[j+1], sub_li[j] 
    return sub_li


'''
Standard answer: 
def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 
'''
assert Sort([['a', 10], ['b', 5], ['c', 20], ['d', 15]]) == [['b', 5], ['a', 10], ['d', 15], ['c', 20]]
assert Sort([['452', 10], ['256', 5], ['100', 20], ['135', 15]]) == [['256', 5], ['452', 10], ['135', 15], ['100', 20]]
assert Sort([['rishi', 10], ['akhil', 5], ['ramya', 20], ['gaur', 15]]) == [['akhil', 5], ['rishi', 10], ['gaur', 15], ['ramya', 20]]
