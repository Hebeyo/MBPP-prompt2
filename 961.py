"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to convert a roman numeral to an integer.
'''

def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    n = len(s)
    if n==1:
        return roman[s]
    res = 0
    for i in range(n-1):
        if roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res+roman[s[-1]]

'''
Standard answer: 
def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
'''
assert roman_to_int('MMMCMLXXXVI')==3986
assert roman_to_int('MMMM')==4000
assert roman_to_int('C')==100
