# minimum number from that lst find 
n=int(input("Enter the number:"))
lst=[]

for i in range(n):
    num=int(input())
    lst.append(num)
minimun=min(lst)
print("output:",minimun)