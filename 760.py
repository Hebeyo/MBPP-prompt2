"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a python function to check whether an array contains only one distinct element or not.
'''

def unique_Element(arr,n):
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            return ('NO')
    return ('YES')

'''
Standard answer: 
def unique_Element(arr,n):
    s = set(arr)
    if (len(s) == 1):
        return ('YES')
    else:
        return ('NO')
'''
assert unique_Element([1,1,1],3) == 'YES'
assert unique_Element([1,2,1,2],4) == 'NO'
assert unique_Element([1,2,3,4,5],5) == 'NO'
