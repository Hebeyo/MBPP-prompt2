"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the surface area of a cone.
'''

def surfacearea_cone(r,h):
  import math
  l = math.sqrt(r * r + h * h)
  SA = math.pi * r * (r + l)
  return SA

'''
Standard answer: 
import math
def surfacearea_cone(r,h):
  l = math.sqrt(r * r + h * h)
  SA = math.pi * r * (r + l)
  return SA
'''
assert surfacearea_cone(5,12)==282.7433388230814
assert surfacearea_cone(10,15)==880.5179353159282
assert surfacearea_cone(19,17)==2655.923961165254
