# filter map reduce
from functools import reduce
lst=[5,2,3,4,3,4,1,2,8,10]
filt=list(filter(lambda x:x%2==0,lst))
print("after filter",filt)

map=list(map(lambda x:x*x,filt))
print("after map",map)

result=reduce(lambda a,b:a+b,map)
print("output of reduce",result)