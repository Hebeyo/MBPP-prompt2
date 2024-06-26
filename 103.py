"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find eulerian number a(n, m).
'''

def eulerian_num(n, m): 
    if (m >= n or n == 0): 
        return 0 
    if (m == 0): 
        return 1 
    return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))

'''
Standard answer: 
def eulerian_num(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
'''
assert eulerian_num(3, 1) == 4
assert eulerian_num(4, 1) == 11
assert eulerian_num(5, 3) == 26
