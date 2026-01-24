# greater number using lambda 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
maximum=lambda a,b : a if a > b else b 
print("maximum number is:",maximum(a,b))
