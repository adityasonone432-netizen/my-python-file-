# return addition of all element from that list
def main():
    try:
        n=int(input("Enter the number of elments:"))
    except ValueError:
        print("Invalid input. please enter an integer")
        return
    lst=[]

    print(f"Enter{n} elements:")
    for i in range(n):
        value=int(input())
        lst.append(value)
    total=sum(lst)
    print(f"output:{total}")
if __name__ == "__main__":
    main()
    

           
