# Question 2 - List Operations

# a. Write a program to find the largest number in a list.
numbers = [10, 25, 8, 45, 12]
print("Largest Number:", max(numbers))

# b. Write a program to remove duplicates from a list.
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicate_list))
print("\nList after removing duplicates:", unique_list)

# c. Write a program to count how many even numbers are in a list.
num_list = [2, 5, 8, 11, 14, 18]
even_count = 0

for num in num_list:
    if num % 2 == 0:
        even_count += 1

print("\nCount of even numbers:", even_count)

# d. Write a program to input 5 numbers and store them in a list.
input_list = []

for i in range(5):
    value = int(input("Enter number: "))
    input_list.append(value)

print("\nEntered List:", input_list)

# e. Write a function that returns the average of all numbers in a list.
def average(lst):
    return sum(lst) / len(lst)

print("\nAverage:", average(input_list))

# f. Convert a string into a list of characters using list().
text = "Python"
char_list = list(text)

print("\nList of Characters:", char_list)

# g. Join all elements of a list into a single string using join().
words = ["Data", "Science", "Python"]
joined = " ".join(words)

print("\nJoined String:", joined)
