# filter map reduce
from functools import reduce
lst=[4,34,36,76,68,24,89,23,86,90,45,70]
filt=list(filter(lambda x:x>=70 and x<=90,lst))
print("after filter",filt)

map=list(map(lambda x: x+10,filt))
print("after map",map)
result=reduce(lambda a,b:a*b,map)
print("output of  reduce",result)
