"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given number is armstrong or not.
'''

def armstrong_number(number):
    sum = 0
    times = 0
    temp = number
    while temp > 0:
        times = times + 1
        temp = temp // 10
    temp = number
    while temp > 0:
        reminder = temp % 10
        sum = sum + (reminder ** times)
        temp //= 10
    if number == sum:
        return True
    else:
        return False

'''
Standard answer: 
def armstrong_number(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
'''
assert armstrong_number(153)==True
assert armstrong_number(259)==False
assert armstrong_number(4458)==False