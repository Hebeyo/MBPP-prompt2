"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the size of the given tuple.
'''

import sys
def tuple_size(tuple_list):
  return (sys.getsizeof(tuple_list))

'''
Standard answer: 
import sys 
def tuple_size(tuple_list):
  return (sys.getsizeof(tuple_list)) 
'''
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
assert tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
assert tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))
