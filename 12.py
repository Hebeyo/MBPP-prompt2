"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to sort a given matrix in ascending order according to the sum of its rows.
'''

def sort_matrix(M):
    result = []
    for i in range(len(M)):
        result.append(sum(M[i]))
    result = [x for _, x in sorted(zip(result, M))]
    return result

'''
Standard answer: 
def sort_matrix(M):
    result = sorted(M, key=sum)
    return result
'''
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]
