"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether an array is subarray of another or not.
'''

def is_Sub_Array(A,B,n,m):
    j = 0
    for i in range(n):
        if A[i] == B[j]:
            j += 1
            if j == m:
                return True
        else:
            j = 0
    return False

'''
Standard answer: 
def is_Sub_Array(A,B,n,m): 
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
'''
assert is_Sub_Array([1,4,3,5],[1,2],4,2) == False
assert is_Sub_Array([1,2,1],[1,2,1],3,3) == True
assert is_Sub_Array([1,0,2,2],[2,2,0],4,3) ==False
