# addition of digits of numbers 
n=int(input("Enter the number:") )
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("sum of digits:",sum)    