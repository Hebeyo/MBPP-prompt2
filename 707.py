"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to count the total set bits from 1 to n.
'''

def count_Set_Bits(n) :  
    n += 1; 
    powerOf2 = 2;   
    cnt = n // 2;  
    while (powerOf2 <= n) : 
        totalPairs = n // powerOf2;  
        cnt += (totalPairs // 2) * powerOf2;  
        if (totalPairs & 1) : 
            cnt += (n % powerOf2) 
        else : 
            cnt += 0
        powerOf2 <<= 1;    
    return cnt;

'''
Standard answer: 
def count_Set_Bits(n) :  
    n += 1; 
    powerOf2 = 2;   
    cnt = n // 2;  
    while (powerOf2 <= n) : 
        totalPairs = n // powerOf2;  
        cnt += (totalPairs // 2) * powerOf2;  
        if (totalPairs & 1) : 
            cnt += (n % powerOf2) 
        else : 
            cnt += 0
        powerOf2 <<= 1;    
    return cnt;  
'''
assert count_Set_Bits(16) == 33
assert count_Set_Bits(2) == 2
assert count_Set_Bits(14) == 28
