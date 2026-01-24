# check whether it is palindrome or not 

num=int(input("Enter the number :"))
original=num
reverse=0
while num>0:
    digit=num%10   #get last digit
    reverse=reverse*10+digit
    num//=10     #remove last digit
if original==reverse:
    print("number is palindrome")
else:
    print("number is not palindrom")   
