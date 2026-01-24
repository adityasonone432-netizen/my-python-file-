 #2 greater number
def ChkGreater(No1,No2):
    if No1>No2:
        print(No1," is greater,")
    else:
        print(No2,"is greater")
ChkGreater(10,20)




ChkGreater=lambda no1,no2:no1 if no1>no2 else no2
print(ChkGreater(10,20),"is greater")