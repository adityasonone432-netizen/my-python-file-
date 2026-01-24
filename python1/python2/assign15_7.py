# returns strings longer than 5 character
num=["Apple","Banana","Mangoes","Grape","Peru"]
longer5=list(filter(lambda a:len(a)>5,num))
print(longer5) 