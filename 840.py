"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the roots of a quadratic equation are numerically equal but opposite in sign or not.
'''

def Check_Solution(a,b,c):  
    if b == 0:  
        return "Yes"  
    else: 
        return "No"

'''
Standard answer: 
def Check_Solution(a,b,c):  
    if b == 0:  
        return ("Yes")  
    else: 
        return ("No")  
'''
assert Check_Solution(2,0,-1) == "Yes"
assert Check_Solution(1,-5,6) == "No"
assert Check_Solution(2,0,2) == "Yes"
