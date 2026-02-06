# prints of thst factor 
n=int(input("Enter the number:"))
print("factors of the number are:")
for i in range(1,n+1):
    if n % i==0:
        print(i,end=" ")