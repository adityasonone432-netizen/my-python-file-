# pyhton application that creates two separate threads named Evenfactor or oddfactor
import threading
def even_list(lst):
    s=0
    for i in lst:
       if i%2 ==0:
           print("Even element:",i)
           s+=i
    print(" sum of even  elements:",s)

def odd_list(lst):
    s=0
    for i in lst:
     if i%2 != 0:
        print("odd element:",i)
        s+=i
    print("sum of odd element:",s)

nums=list(map(int,input("Enter list number:").split()))

t1=threading.Thread(target=even_list,args=(nums,))        
t2=threading.Thread(target=odd_list,args=(nums,))        

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main program")






   
