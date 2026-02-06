# maximum number from that lst
n=int(input("Enter the number:"))
lst=[]

for i in range(n):
    num=int(input())
    lst.append(num)
maximun=max(lst)
print("output:",maximun)