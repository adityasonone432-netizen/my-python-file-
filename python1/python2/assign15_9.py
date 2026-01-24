# reduce product of all element 
from functools import reduce
num=[1,2,3,4,2,2]
mul=lambda numbers:reduce(lambda a,b:a*b,num)
print("multiplication is:",mul(num))