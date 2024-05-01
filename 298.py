"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to find the nested list elements which are present in another list.
'''

def intersection_nested_lists(l1, l2):
    result = []
    for lst in l2:
        temp = []
        for n in lst:
            if n in l1:
                temp.append(n)
        result.append(temp)
    return result

'''
Standard answer: 
def intersection_nested_lists(l1, l2):
    result = [[n for n in lst if n in l1] for lst in l2]
    return result
'''
assert intersection_nested_lists( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==[[12], [7, 11], [1, 5, 8]]
assert intersection_nested_lists([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]])==[[], []]
assert intersection_nested_lists(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']])==[['john'], ['john'], ['john'], []]
