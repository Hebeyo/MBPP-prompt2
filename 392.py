"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
'''

def get_max_sum(n):
    res = [0, 1]
    i = 2
    while i < n + 1:
        res.append(max(i, res[int(i / 2)] + res[int(i / 3)] + res[int(i / 4)] + res[int(i / 5)]))
        i += 1
    return res[n]

'''
Standard answer: 
def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
'''
assert get_max_sum(60) == 106
assert get_max_sum(10) == 12
assert get_max_sum(2) == 2
