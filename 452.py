"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function that gives loss amount if the given amount has loss else return none.
'''

def loss_amount(actual_cost,sale_amount): 
  if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    return amount
  else:
    return None

'''
Standard answer: 
def loss_amount(actual_cost,sale_amount): 
  if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    return amount
  else:
    return None
'''
assert loss_amount(1500,1200)==None
assert loss_amount(100,200)==100
assert loss_amount(2000,5000)==3000
