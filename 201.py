"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""


'''Write a python function to check whether the elements in a list are same or not.
'''

def chkList(lst):
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            return False
    return True

'''
Standard answer: 
def chkList(lst): 
    return len(set(lst)) == 1
'''
assert chkList(['one','one','one']) == True
assert chkList(['one','Two','Three']) == False
assert chkList(['bigdata','python','Django']) == False
