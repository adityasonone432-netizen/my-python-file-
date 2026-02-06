# # return largest of three number 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third  number:"))
largest=lambda x,y,z : x if (x>=y and x>=z) else (y if y>=z else z)
print("largest number is",largest(a,b,c))
