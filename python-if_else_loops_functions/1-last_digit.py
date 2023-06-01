#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
n = last * -1

if number < 0:
    positivo = number * -1
    last = positivo % 10
    if last != 0:
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} is 0")
elif last < 6 and last > 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
else:
    print(f"Last digit of {number} is {last} is 0")
