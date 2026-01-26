# find min and max 

import threading
def find_max(lst):
    print("maximum:",max(lst))

def find_min(lst):
        print("minimum:",min(lst))
nums=list(map(int,input().split()))

t1=threading.Thread(target=find_max,args=(nums,))
t2=threading.Thread(target=find_min,args=(nums,))


t1.start()
t2.start()

t1.join()
t2.join()

