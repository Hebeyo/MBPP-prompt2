"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be mindful to choose better-performing function interfaces when calling functions, avoiding unnecessary deep recursion."""

'''Write a function to find the greatest common divisor (gcd) of two integers by using recursion.
'''

def recur_gcd(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
	elif a == b:
		return a
	elif a > b:
		return recur_gcd(a-b, b)
	else:
		return recur_gcd(a, b-a)

'''
Standard answer: 
def recur_gcd(a, b):
	low = min(a, b)
	high = max(a, b)
	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return recur_gcd(low, high%low)
'''
assert recur_gcd(12,14) == 2
assert recur_gcd(13,17) == 1
assert recur_gcd(9, 3) == 3
