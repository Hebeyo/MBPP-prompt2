"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to select the nth items of a list.
'''

def nth_items(list,n):
    new_list=[]
    for i in range(0,len(list),n):
        new_list.append(list[i])
    return new_list

'''
Standard answer: 
def nth_items(list,n):
 return list[::n]
'''
assert nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9],2)==[1, 3, 5, 7, 9] 
assert nth_items([10,15,19,17,16,18],3)==[10,17] 
assert nth_items([14,16,19,15,17],4)==[14,17]
