# pyhton application that creates two separate threads named Evenfactor or oddfactor
import threading
def even_facter(n):
    s=0
    for i in range(1,n+1):
       if n%i == 0 and i%2==0:
           print("Even factor:",i)
           s+=i
    print(" sum of even  factors:",s)
def odd_facter(n):
    s=0
    for i in range(1,n+1):
     if n%i == 0 and i% 2!= 0:
        print("odd factor:",i)
        s+=i
    print("sum of odd factors:",s)

num=int(input("Enter number:"))

t1=threading.Thread(target=even_facter,args=(num,))        
t2=threading.Thread(target=odd_facter,args=(num,))        

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main program")






   
