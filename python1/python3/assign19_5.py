# filter map reduce

from functools import reduce

lst=[2,70,11,10,17,23,31,77]

filt=list(filter(lambda x: x>1 and all (x%i != 0  for i in range(2,x)),lst))
print("after filter",filt)

map=list(map(lambda x:x*2,filt))
print("after map",map)

result=reduce(lambda a,b: a if a>b else b,map)
print("output of reduce",result)    