"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to find the list of lists with maximum length.
'''

def max_length(list1):
    max_length = 0
    max_list = []
    for x in list1:
        if len(x) > max_length:
            max_length = len(x)
            max_list = x
    return(max_length, max_list)


'''
Standard answer: 
def max_length(list1):
    max_length = max(len(x) for x in  list1 )  
    max_list = max((x) for x in   list1)
    return(max_length, max_list)
'''
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
assert max_length([[5], [15,20,25]])==(3, [15,20,25])
