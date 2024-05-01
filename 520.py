"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Be sure to use efficient algorithms, minimize unnecessary conditional statements, and for mathematical problems, prioritize algorithms that can exploit mathematical properties."""

'''Write a function to find the lcm of the given array elements.
'''

def get_lcm(l):
  lcm = max(l)
  while True:
    if all(lcm % i == 0 for i in l):
      return lcm
    lcm += max(l)

'''
Standard answer: 
def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	while (rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm 
def get_lcm(l):
  num1 = l[0]
  num2 = l[1]
  lcm = find_lcm(num1, num2)
  for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])
  return lcm 
'''
assert get_lcm([2, 7, 3, 9, 4]) == 252
assert get_lcm([1, 2, 8, 3]) == 24
assert get_lcm([3, 8, 4, 10, 5]) == 120
