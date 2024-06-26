"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find sum and average of first n natural numbers.
'''

def sum_average(number):
    total = 0
    for value in range(1, number + 1):
        total = total + value
    average = total / number
    return (total,average)

'''
Standard answer: 
def sum_average(number):
 total = 0
 for value in range(1, number + 1):
    total = total + value
 average = total / number
 return (total,average)
'''
assert sum_average(10)==(55, 5.5)
assert sum_average(15)==(120, 8.0)
assert sum_average(20)==(210, 10.5)
