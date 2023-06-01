#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n % 10 > 5:
    print(f"Last digit of {n} is {n % 10} and is greater than 5")
if n % 10 == 0:
    print(f"Last digit of {n} is {n % 10} and is 0")
if n % 10 < 6 and number % 10 != 0 and number > 0:
    print(f"Last digit of {n} is {n % 10} and is less than 6 and not 0")
if n < 0:
    np = number * -1
    print(f"Last digit of {n} is {np % 10 * -1} and is less than 6 and not 0")
