# pyhton application that creates two separate threads named Evenfactor or oddfactor
import threading

def small_char(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Lowercase count:", count)
    print()

def capital_char(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Uppercase count:", count)
    print()

def digit_char(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Digit count:", count)
    print()

text = input("Enter string: ")

t1 = threading.Thread(target=small_char, args=(text,), name="Small")
t2 = threading.Thread(target=capital_char, args=(text,), name="Capital")
t3 = threading.Thread(target=digit_char, args=(text,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Exit from main")