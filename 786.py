"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to locate the right insertion point for a specified value in sorted order.
'''

def right_insertion(a, x):
    for i in range(len(a)):
        if a[i] >= x:
            return i
    return len(a)

'''
Standard answer: 
import bisect
def right_insertion(a, x):
    i = bisect.bisect_right(a, x)
    return i
'''
assert right_insertion([1,2,4,5],6)==4
assert right_insertion([1,2,4,5],3)==2
assert right_insertion([1,2,4,5],7)==4
