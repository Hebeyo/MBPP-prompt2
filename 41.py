"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to filter even numbers using lambda function.
'''

def filter_evennumbers(nums):
    even_nums=[]
    for i in nums:
        if i%2==0:
            even_nums.append(i)
    return even_nums

'''
Standard answer: 
def filter_evennumbers(nums):
 even_nums = list(filter(lambda x: x%2 == 0, nums))
 return even_nums
'''
assert filter_evennumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2, 4, 6, 8, 10]
assert filter_evennumbers([10,20,45,67,84,93])==[10,20,84]
assert filter_evennumbers([5,7,9,8,6,4,3])==[8,6,4]
