# filter count even number of list 

num=[1,2,3,4,5,6,8,5,11,12,20]
even=len(list(filter(lambda a:a%2==0,num)))
print("count even is:",even)

