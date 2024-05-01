"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
"""Pay attention to integrating programming language features, use efficient built-in modules of the programming language, avoid poor exception handling, and reduce unused local variables."""

'''Write a function to check if the given expression is balanced or not.
'''

def check_expression(exp):
    stack = []
    for i in exp:
        if i in ['(', '{', '[']:
            stack.append(i)
        else:
            if not stack:
                return False
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

'''
Standard answer: 
from collections import deque
def check_expression(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
'''
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{]") == False
assert check_expression("{()}[{}][]({})") == True
