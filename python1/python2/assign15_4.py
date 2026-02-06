# return the addition of all element 
from functools import reduce    # reduce() not by default it import
num=[1,2,3,4,6,7,8]
addition= lambda nummbers: reduce(lambda a,b:a+b,num) 
print(addition(num)) 