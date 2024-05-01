"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to remove characters from the first string which are present in the second string.
'''

def remove_dirty_chars(string, second_string):
    temp = []
    for x in string:
        temp.append(x)
    count = [0] * 256
    for i in second_string:
        count[ord(i)] += 1
    ip_ind = 0
    res_ind = 0
    while ip_ind != len(temp):
        temp_char = temp[ip_ind]
        if count[ord(temp_char)] == 0:
            temp[res_ind] = temp[ip_ind]
            res_ind += 1
        ip_ind += 1
    return ''.join(temp[0:res_ind])

'''
Standard answer: 
NO_OF_CHARS = 256
def str_to_list(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 
def lst_to_string(List): 
	return ''.join(List) 
def get_char_count_array(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def remove_dirty_chars(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
'''
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles' 
