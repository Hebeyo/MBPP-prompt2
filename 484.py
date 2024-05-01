"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove the matching tuples from the given two tuples.
'''

def remove_matching_tuple(test_list1, test_list2):
  res = []
  for sub in test_list1:
    if sub not in test_list2:
      res.append(sub)
  return (res)

'''
Standard answer: 
def remove_matching_tuple(test_list1, test_list2):
  res = [sub for sub in test_list1 if sub not in test_list2]
  return (res) 
'''
assert remove_matching_tuple([('Hello', 'dude'), ('How', 'are'), ('you', '?')], [('Hello', 'dude'), ('How', 'are')]) == [('you', '?')]
assert remove_matching_tuple([('Part', 'of'), ('the', 'journey'), ('is ', 'end')], [('Journey', 'the'), ('is', 'end')]) == [('Part', 'of'), ('the', 'journey'), ('is ', 'end')]
assert remove_matching_tuple([('Its', 'been'), ('a', 'long'), ('day', 'without')], [('a', 'long'), ('my', 'friend')]) == [('Its', 'been'), ('day', 'without')]
