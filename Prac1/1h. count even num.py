#1h. Print Squares from 1 to 10 and count even num

print("Squares from 1 to 10")

for i in range(1, 11):
    print(i, "=", i * i)

count = 0

for i in range(5):
    num = int(input("Enter number: "))

    if num % 2 == 0:
        count += 1

print("Total Even Numbers =", count)
