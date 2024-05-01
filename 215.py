"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Avoid string concatenations and assignments within loops, and optimize the code structure to reduce multiple loops."""

'''Write a function to decode a run-length encoded given list.
'''

def decode_list(alist):
    decoded_list = []
    for i in alist:
        if isinstance(i, list):
            decoded_list.extend([i[1]]*i[0])
        else:
            decoded_list.append(i)
    return decoded_list

'''
Standard answer: 
def decode_list(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]
'''
assert decode_list([[2, 1], 2, 3, [2, 4], 5,1])==[1,1,2,3,4,4,5,1]
assert decode_list(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y'])==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']
assert decode_list(['p', 'y', 't', 'h', 'o', 'n'])==['p', 'y', 't', 'h', 'o', 'n']
