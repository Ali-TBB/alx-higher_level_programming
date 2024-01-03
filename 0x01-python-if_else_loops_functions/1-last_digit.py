#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

a = abs(number) % 10

if a < 6 and a != 0:
    print("Last digit of",number, "is" ,a, "and is less than 6 and not 0")

elif a > 5 and a != 0:
    print("Last digit of" ,number, "is" ,a, "and is greater than 5")
else:
    print(f'Last digit of {number} is {last} and is 0')