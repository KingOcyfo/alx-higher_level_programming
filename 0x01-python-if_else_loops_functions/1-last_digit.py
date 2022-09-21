#!/usr/bin/python3
import random
number = random.randint(-10000 10000)
1d = abs(number) % 10
if number < 0:
    1d *= -1
fmt = f"Last digit of {number:d} is {1d:d} and is"
if 1d > 5:
    print(f"{fmt:s} greater than 5")
elif 1d == 0:
    print(f"{fmt:s} 0")
else:
    print(f"{fmt:s} less than 6 and not 0")
