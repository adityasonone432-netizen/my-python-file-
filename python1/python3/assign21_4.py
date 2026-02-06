import threading

nums = list(map(int, input("Enter numbers: ").split()))

sum_result = 0
product_result = 1

def calc_sum():
    global sum_result
    sum_result = sum(nums)

def calc_product():
    global product_result
    for n in nums:
        product_result *= n

t1 = threading.Thread(target=calc_sum)
t2 = threading.Thread(target=calc_product)

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum =", sum_result)
print("Product =", product_result)