"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given amount has no profit and no loss
'''

def noprofit_noloss(actual_cost,sale_amount): 
  if actual_cost == sale_amount:
    return True
  else:
    return False

'''
Standard answer: 
def noprofit_noloss(actual_cost,sale_amount): 
  if(sale_amount == actual_cost):
    return True
  else:
    return False
'''
assert noprofit_noloss(1500,1200)==False
assert noprofit_noloss(100,100)==True
assert noprofit_noloss(2000,5000)==False
