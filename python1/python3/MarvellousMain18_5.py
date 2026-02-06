# module marvellous 
import MarvellousNum18_5
def Listprime(lst):
    total=0
    for x in lst:
        if MarvellousNum18_5.Chkprime(x):
            total=total+x
    return total


n=int(input("Enter the number of element:"))
lst=[]

for i in range(n):
    num=int(input())
    lst.append(num)
result=Listprime(lst)
print("output:",result)