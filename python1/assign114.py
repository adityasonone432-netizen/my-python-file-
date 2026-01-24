# reverse number 
n=int(input("Enter the number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print("sum of digit =",reverse)    