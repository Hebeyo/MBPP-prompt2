"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a python function to find the maximum occurring character in a given string.
'''

def get_max_occuring_char(str1):
  max_count = 0
  max_char = ''
  for i in set(str1):
    if str1.count(i) > max_count:
      max_count = str1.count(i)
      max_char = i
  return max_char

'''
Standard answer: 
def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch
'''
assert get_max_occuring_char("data") == "a"
assert get_max_occuring_char("create") == "e"
assert get_max_occuring_char("brilliant girl") == "i"
