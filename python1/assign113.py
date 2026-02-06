#sum of digits
num=int(input ("Enter the number:"))
sumdigit=0

while num>0:
    sumdigit+=num%10
    num//=10
print("sum of digit =",sumdigit)
 

