"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to count the most common words in a dictionary.
'''

from collections import Counter
def count_common(words):
  result = []
  word_counts = Counter(words)
  top_four = word_counts.most_common(4)
  for i in top_four:
    result.append(i)
  return result

'''
Standard answer: 
from collections import Counter
def count_common(words):
  word_counts = Counter(words)
  top_four = word_counts.most_common(4)
  return (top_four)

'''
assert count_common(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
assert count_common(['one', 'two', 'three', 'four', 'five', 'one', 'two', 'one', 'three', 'one']) == [('one', 4), ('two', 2), ('three', 2), ('four', 1)]
assert count_common(['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google', 'Apple', 'Netflix', 'Amazon']) == [('Apple', 2), ('Amazon', 2), ('Netflix', 2), ('Facebook', 1)]
