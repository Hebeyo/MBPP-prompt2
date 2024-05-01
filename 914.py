"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given string is made up of two alternating characters or not.
'''

def is_Two_Alter(s):  
    for i in range (len( s) - 2) : 
        if (s[i] != s[i + 2]) : 
            return False
    if (s[0] == s[1]): 
        return False
    return True

'''
Standard answer: 
def is_Two_Alter(s):  
    for i in range (len( s) - 2) : 
        if (s[i] != s[i + 2]) : 
            return False
    if (s[0] == s[1]): 
        return False
    return True
'''
assert is_Two_Alter("abab") == True
assert is_Two_Alter("aaaa") == False
assert is_Two_Alter("xyz") == False
