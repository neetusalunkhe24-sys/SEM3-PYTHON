#1f. max min

numbers = [12, 45, 7, 89, 23, 56, 78, 34, 90, 11]

print("List:", numbers)

print("Maximum =", max(numbers))
print("Minimum =", min(numbers))
print("Average =", sum(numbers) / len(numbers))

print("Ascending Order =", sorted(numbers))
print("Descending Order =", sorted(numbers, reverse=True))

new_num = int(input("Enter a new number: "))
numbers.append(new_num)

numbers.pop(0)

print("Updated List =", numbers)
