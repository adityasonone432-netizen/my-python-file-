# return true number is even 
num=int(input("Enter the number:"))
even=lambda n: True if n%2==0 else False
print("number is",even(num))