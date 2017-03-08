import random
import types

def lottery():
    for i in range(6):
        print("under for loop")
        yield random.randint(1,40)

        # yield random.randint(1,15)

for random_number in lottery():
    print(random_number)

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b
    pass

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
print()
print (sum(firstn(12)))
