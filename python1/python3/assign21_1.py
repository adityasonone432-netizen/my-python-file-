# prime non prime 
import threading
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(lst):
    print("Thread Name:", threading.current_thread().name)
    for n in lst:
        if is_prime(n):
            print("Prime:", n)
    print()

def nonprime_list(lst):
    print("Thread Name:", threading.current_thread().name)
    for n in lst:
        if not is_prime(n):
            print("Non-Prime:", n)
    print()

nums = list(map(int, input("Enter numbers: ").split()))

t1 = threading.Thread(target=prime_list, args=(nums,), name="Prime")
t2 = threading.Thread(target=nonprime_list, args=(nums,), name="NonPrime")

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
