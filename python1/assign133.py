# checking number is perfect or not 
n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("number is a perfect number ") 
else:
    print("number is not perfect number")       