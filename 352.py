"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a python function to check whether all the characters in a given string are unique.
'''

def unique_Characters(str):
    return len(set(str)) == len(str)

'''
Standard answer: 
def unique_Characters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if (str[i] == str[j]):
                return False;
    return True;
'''
assert unique_Characters('aba') == False
assert unique_Characters('abc') == True
assert unique_Characters('abab') == False
