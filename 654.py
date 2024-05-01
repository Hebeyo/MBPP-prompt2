"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the perimeter of a rectangle.
'''

def rectangle_perimeter(l,b):
  perimeter=2*(l+b)
  return perimeter

'''
Standard answer: 
def rectangle_perimeter(l,b):
  perimeter=2*(l+b)
  return perimeter
'''
assert rectangle_perimeter(10,20)==60
assert rectangle_perimeter(10,5)==30
assert rectangle_perimeter(4,2)==12
