"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the number of rectangles in a circle of radius r.
'''

def count_Rectangles(radius):  
    rectangles = 0 
    diameter = 2 * radius 
    diameterSquare = diameter * diameter 
    for a in range(1, 2 * radius):  
        for b in range(1, 2 * radius): 
            diagnalLengthSquare = (a * a +  b * b)  
            if (diagnalLengthSquare <= diameterSquare) : 
                rectangles += 1
    return rectangles

'''
Standard answer: 
def count_Rectangles(radius):  
    rectangles = 0 
    diameter = 2 * radius 
    diameterSquare = diameter * diameter 
    for a in range(1, 2 * radius):  
        for b in range(1, 2 * radius): 
            diagnalLengthSquare = (a * a +  b * b)  
            if (diagnalLengthSquare <= diameterSquare) : 
                rectangles += 1
    return rectangles 
'''
assert count_Rectangles(2) == 8
assert count_Rectangles(1) == 1
assert count_Rectangles(0) == 0
