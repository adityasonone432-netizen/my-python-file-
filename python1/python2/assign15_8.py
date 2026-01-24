# filter number divisible 5 and 3
num=[4,15,20,21,12,10,30]
div=list(filter(lambda a:a%3==0 and a%5==0, num))
print(div)
