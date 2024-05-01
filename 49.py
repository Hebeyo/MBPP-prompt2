"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to extract every first or specified element from a given two-dimensional list.
'''

def specified_element(nums, N):
    result = []
    for i in nums:
        result.append(i[N])
    return result

'''
Standard answer: 
def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result
    
'''
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],1)==[2,5,1]
