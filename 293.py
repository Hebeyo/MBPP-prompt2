"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the third side of a right angled triangle.
'''

def otherside_rightangle(w,h):
  s=(w**2+h**2)**0.5
  return s


'''
Standard answer: 
import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s
'''
assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685
