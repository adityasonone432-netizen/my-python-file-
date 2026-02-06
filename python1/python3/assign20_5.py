# print 1 to 50 and reverse this in trhead

import threading

def thread1():
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    for i in range(1, 51):
        print(i)
    print()

def thread2():
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    for i in range(50, 0, -1):
        print(i)
    print()

t1 = threading.Thread(target=thread1, name="Thread1")
t2 = threading.Thread(target=thread2, name="Thread2")

t1.start()
t1.join()      # synchronization

t2.start()
t2.join()

print("Exit from main")
