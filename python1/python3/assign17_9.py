# display numbers
n=int(input("Enter the number:") )
count=0
while n>0:
    count+=1
    n=n//10
print("Number of digits:",count)    