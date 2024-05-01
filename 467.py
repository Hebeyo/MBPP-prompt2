"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to convert decimal number to octal number.
'''

def decimal_to_Octal(deciNum):
    octalNum = 0
    countval = 1;
    dNo = deciNum;
    while (deciNum!= 0):
        remainder= deciNum % 8;
        octalNum+= remainder*countval;
        countval= countval*10;
        deciNum //= 8; 
    return (octalNum)

'''
Standard answer: 
def decimal_to_Octal(deciNum):
    octalNum = 0
    countval = 1;
    dNo = deciNum;
    while (deciNum!= 0):
        remainder= deciNum % 8;
        octalNum+= remainder*countval;
        countval= countval*10;
        deciNum //= 8; 
    return (octalNum)
'''
assert decimal_to_Octal(10) == 12
assert decimal_to_Octal(2) == 2
assert decimal_to_Octal(33) == 41
