#1c. square root of a number

import math

while True:
    num  = input("Enter number (or type 'q' to quit):")

    if num.lower() == "q":
        break

    num = float(num)

    if num < 0:
        print("Square root not possible")
    else:
        print("Square root =", math.sqrt(num))
