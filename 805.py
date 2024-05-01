"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to find the list in a list of lists whose sum of elements is the highest.
'''

def max_sum_list(lists):
    max_sum = -1
    max_list = []
    for i in lists:
        if sum(i) > max_sum:
            max_sum = sum(i)
            max_list = i
    return max_list

'''
Standard answer: 
def max_sum_list(lists):
 return max(lists, key=sum)
'''
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12] 
assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10] 
assert max_sum_list([[2,3,1]])==[2,3,1] 
