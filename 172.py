"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the occurence of characters 'std' in the given string 1. list item 1. list item 1. list item 2. list item 2. list item 2. list item
'''

def count_occurance(s):
  count=0
  for i in range(len(s)-2):
    if (s[i:i+3] == 'std'):
      count = count + 1
  return count

'''
Standard answer: 
def count_occurance(s):
  count=0
  for i in range(len(s)):
    if (s[i]== 's' and s[i+1]=='t' and s[i+2]== 'd'):
      count = count + 1
  return count
'''
assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("truststdsolensporsd") == 1
assert count_occurance("makestdsostdworthit") == 2
