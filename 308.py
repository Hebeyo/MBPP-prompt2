"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to find the specified number of largest products from two given lists.
'''

def large_product(nums1, nums2, N):
    result = []
    for x in nums1:
        for y in nums2:
            result.append(x*y)
    result = sorted(result, reverse=True)[:N]
    return result

'''
Standard answer: 
def large_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
    return result
'''
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)==[60, 54, 50, 48]
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)==[60, 54, 50, 48, 45]
