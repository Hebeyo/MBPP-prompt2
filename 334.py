"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the triangle is valid or not if sides are given.
'''

def check_Validity(a,b,c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True

'''
Standard answer: 
def check_Validity(a,b,c):  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        
'''
assert check_Validity(1,2,3) == False
assert check_Validity(2,3,5) == False
assert check_Validity(7,10,5) == True
