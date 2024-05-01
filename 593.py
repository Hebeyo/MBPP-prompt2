"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to remove leading zeroes from an ip address.
'''

def removezero_ip(ip):
  ip = ip.split('.')
  for i in range(len(ip)):
    ip[i] = str(int(ip[i]))
  return '.'.join(ip)

'''
Standard answer: 
import re
def removezero_ip(ip):
 string = re.sub('\.[0]*', '.', ip)
 return string
'''
assert removezero_ip("216.08.094.196")==('216.8.94.196') 
assert removezero_ip("12.01.024")==('12.1.24') 
assert removezero_ip("216.08.094.0196")==('216.8.94.196') 
