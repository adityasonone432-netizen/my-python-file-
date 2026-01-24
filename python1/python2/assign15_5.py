#returns the maximum element
from functools import reduce
num=[4,8,9,1,2,5,12,3,]
largest=lambda numbers:reduce(lambda a,b:a if a>b else b,numbers)
print("largest number is",largest(num))
