"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to count those characters which have vowels as their neighbors in the given string.
'''

def count_vowels(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res)

'''
Standard answer: 
def count_vowels(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
'''
assert count_vowels('bestinstareels') == 7
assert count_vowels('partofthejourneyistheend') == 12
assert count_vowels('amazonprime') == 5
