"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to find the maximum length of sublist.
'''

def Find_Max_Length(lst):  
    maxLength = 0
    for i in lst:
        if len(i) > maxLength:
            maxLength = len(i)
    return maxLength

'''
Standard answer: 
def Find_Max_Length(lst):  
    maxLength = max(len(x) for x in lst )
    return maxLength 
'''
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
assert Find_Max_Length([[0,1],[2,2,],[3,2,1]]) == 3
assert Find_Max_Length([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5
