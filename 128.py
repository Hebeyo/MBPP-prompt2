"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to shortlist words that are longer than n from a given list of words.
'''

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len


'''
Standard answer: 
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
'''
assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(2,"writing a program")==['writing','program']
assert long_words(5,"sorting list")==['sorting']
