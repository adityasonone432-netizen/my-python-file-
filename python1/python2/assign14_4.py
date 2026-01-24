# returns minimum number 
a= int(input("Enter the  first  number:"))
b= int(input("Enter the  second  number:"))
minimum=lambda a,b : a if a < b else b
print("minimun number is :",minimum(a,b))


