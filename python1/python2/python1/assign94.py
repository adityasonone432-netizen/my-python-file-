
#mtd1 cube of number 
def cube(num):
    cube=num**3
    print("cube of the number:",cube)
num=int(input("Enter the number:"))
cube(num)


#mtd2 cube of number
num=int(input("Enter the number:"))
cube=num**3
print("cube of number is:",cube)


cube=lambda num:num**3
num=int(input("Enter the number:"))
print("cube of  the number  ",cube(num))