"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to generate a two-dimensional array.
'''

def multi_list(rownum,colnum):
  multi_list = []
  for row in range(rownum):
    multi_list.append([])
    for col in range(colnum):
      multi_list[row].append(row*col)
  return multi_list

'''
Standard answer: 
def multi_list(rownum,colnum):
  multi_list = [[0 for col in range(colnum)] for row in range(rownum)]
  for row in range(rownum):
    for col in range(colnum):
        multi_list[row][col]= row*col
  return multi_list

'''
assert multi_list(3,4)==[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 
assert multi_list(5,7)==[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6], [0, 2, 4, 6, 8, 10, 12], [0, 3, 6, 9, 12, 15, 18], [0, 4, 8, 12, 16, 20, 24]]
assert multi_list(10,15)==[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42], [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56], [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70], [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84], [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98], [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112], [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]]
