"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to sort counter by value.
'''

def sort_counter(dict1):
    list1 = []
    for key, value in dict1.items():
        list1.append((value,key))
    list1.sort(reverse=True)
    return [(i[1],i[0]) for i in list1]

'''
Standard answer: 
from collections import Counter
def sort_counter(dict1):
 x = Counter(dict1)
 sort_counter=x.most_common()
 return sort_counter
'''
assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
assert sort_counter({'Math':400, 'Physics':300, 'Chemistry':250})==[('Math', 400), ('Physics', 300), ('Chemistry', 250)]
assert sort_counter({'Math':900, 'Physics':1000, 'Chemistry':1250})==[('Chemistry', 1250), ('Physics', 1000), ('Math', 900)]
