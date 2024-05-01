"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to find common divisor between two numbers in a given pair.
'''

def num_comm_div(x, y):
  i = 1
  gcd = 0
  while(i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
      gcd = i;
    i += 1
  result = 0
  z = int(gcd**0.5)
  i = 1
  while(i <= z):
    if(gcd % i == 0):
      result += 2 
      if(i == gcd/i):
        result -= 1
    i += 1
  return result

'''
Standard answer: 
def ngcd(x,y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x,y):
  n = ngcd(x,y)
  result = 0
  z = int(n**0.5)
  i = 1
  while(i <= z):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result
'''
assert num_comm_div(2,4) == 2
assert num_comm_div(2,8) == 2
assert num_comm_div(12,24) == 6
