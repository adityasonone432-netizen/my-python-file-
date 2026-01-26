# accept one another number from user and return frequency of that num from lst
n=int(input("Enter the number of element:"))
lst=[]

for i in range(n):
    num=int(input())
    lst.append(num)
search=int(input("Enter element to search:"))
count=lst.count(search)
print("output:",count)