"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to find the volume of a cone.
'''

def volume_cone(r,h):
  volume = (1.0/3) * 3.14159265358979323846 * r * r * h
  return volume

'''
Standard answer: 
import math
def volume_cone(r,h):
  volume = (1.0/3) * math.pi * r * r * h
  return volume
'''
assert volume_cone(5,12)==314.15926535897927
assert volume_cone(10,15)==1570.7963267948965
assert volume_cone(19,17)==6426.651371693521
