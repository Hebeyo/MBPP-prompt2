"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a python function to find the sum of repeated elements in a given array.
'''

def find_Sum(arr,n): 
    sum = 0
    for i in range(n): 
        if arr.count(arr[i]) > 1: 
            sum += arr[i] 
    return sum

'''
Standard answer: 
def find_Sum(arr,n): 
    return sum([x for x in arr if arr.count(x) > 1])
'''
assert find_Sum([1,2,3,1,1,4,5,6],8) == 3
assert find_Sum([1,2,3,1,1],5) == 3
assert find_Sum([1,1,2],3) == 2
assert find_Sum([1,1,2,3,4,5,6,3,5],9) == 18
