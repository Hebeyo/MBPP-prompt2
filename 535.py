"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the top or bottom surface area of a cylinder.
'''

def topbottom_surfacearea(r):
  toporbottomarea=3.1415*r*r
  return toporbottomarea

'''
Standard answer: 
def topbottom_surfacearea(r):
  toporbottomarea=3.1415*r*r
  return toporbottomarea
'''
assert topbottom_surfacearea(10)==314.15000000000003
assert topbottom_surfacearea(5)==78.53750000000001
assert topbottom_surfacearea(4)==50.264
