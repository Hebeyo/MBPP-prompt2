"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find lcm of two positive integers.
'''

def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y
   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return lcm

'''
Standard answer: 
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y
   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return lcm
'''
assert lcm(4,6) == 12
assert lcm(15,17) == 255
assert lcm(2,6) == 6
