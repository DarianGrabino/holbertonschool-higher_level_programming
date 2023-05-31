#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10

if number < 0:
    positivo = number * -1
    last = positivo % 10
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
elif last_digit < 6 and last_digit > 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
else:
    print(f"Last digit of {number} is {last} is 0")
