
#check whether number divisible 3 and 5
num=int(input("Enter the number:"))
if num % 3 == 0 and num %  5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5 ")


    # mtd2 
    def Checkdivisible(num):
        if num % 3 == 0 and num % 5 == 0:
            print("The number is divisible by both 3 and 5")
        else:
            print("The number is not divisibe by 3 and 5")
            num=int(input("Enter the number:"))
            Checkdivisible(num)
