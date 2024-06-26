"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count occurences of a character in a repeated string.
'''

def count_Char(str,x): 
    count = 0
    for i in range(len(str)):  
        if (str[i] == x) : 
            count += 1
    n = 10
    repititions = n // len(str)  
    count = count * repititions  
    l = n % len(str)  
    for i in range(l): 
        if (str[i] == x):  
            count += 1
    return count

'''
Standard answer: 
def count_Char(str,x): 
    count = 0
    for i in range(len(str)):  
        if (str[i] == x) : 
            count += 1
    n = 10
    repititions = n // len(str)  
    count = count * repititions  
    l = n % len(str)  
    for i in range(l): 
        if (str[i] == x):  
            count += 1
    return count  
'''
assert count_Char("abcac",'a') == 4
assert count_Char("abca",'c') == 2
assert count_Char("aba",'a') == 7
