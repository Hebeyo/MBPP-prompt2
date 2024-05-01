"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to perform chunking of tuples each of size n.
'''

def chunk_tuples(test_tup, N):
    res = []
    for i in range(0, len(test_tup), N):
        res.append(test_tup[i : i + N])
    return (res)

'''
Standard answer: 
def chunk_tuples(test_tup, N):
  res = [test_tup[i : i + N] for i in range(0, len(test_tup), N)]
  return (res) 
'''
assert chunk_tuples((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
assert chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 2) == [(1, 2), (3, 4), (5, 6), (7, 8), (9,)]
assert chunk_tuples((11, 14, 16, 17, 19, 21, 22, 25), 4) == [(11, 14, 16, 17), (19, 21, 22, 25)]
