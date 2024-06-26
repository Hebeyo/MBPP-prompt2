"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether one root of the quadratic equation is twice of the other or not.
'''

def Check_Solution(a,b,c): 
    if (2*b*b == 9*a*c): 
        return ("Yes"); 
    else: 
        return ("No");

'''
Standard answer: 
def Check_Solution(a,b,c): 
    if (2*b*b == 9*a*c): 
        return ("Yes"); 
    else: 
        return ("No"); 
'''
assert Check_Solution(1,3,2) == "Yes"
assert Check_Solution(1,2,3) == "No"
assert Check_Solution(1,-5,6) == "No"
