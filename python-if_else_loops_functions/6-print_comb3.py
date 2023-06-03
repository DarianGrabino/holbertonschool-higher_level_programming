#!/usr/bin/python3

for n in range(0, 9):
    for i in range(0, 10):
        if (n > i) or (n == i):
            continue
        else:
            print(f"{n}{i}", end="")
        if (n < 8):
            print(", ", end="")
print()
