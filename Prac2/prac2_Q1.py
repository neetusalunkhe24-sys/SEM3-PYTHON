# Question 1 - Tuple Operations

# a. Create a tuple with 5 elements and print it
subjects = ("Python", "OS", "Scala", "DBMS", "DS")
print("Original Tuple:", subjects)

# b. Access first and last elements
print("\nFirst Element:", subjects[0])
print("Last Element:", subjects[-1])

# c. Slice tuple and print middle 3 elements
print("\nMiddle 3 Elements:", subjects[1:4])

# d. Concatenate two tuples
extra_subjects = ("AI", "ML")
combined = subjects + extra_subjects
print("\nConcatenated Tuple:", combined)

# e. Reverse tuple using slicing
reversed_tuple = subjects[::-1]
print("\nReversed Tuple:", reversed_tuple)

# f. Count occurrence of an element
count_tuple = ("Python", "OS", "Python", "DBMS", "Python")
print("\nCount of Python:", count_tuple.count("Python"))

# g. Find index of specific element
print("\nIndex of Scala:", subjects.index("Scala"))

# h. Check if element exists
search = "DBMS"

if search in subjects:
    print("\nDBMS exists in tuple")
else:
    print("\nDBMS does not exist")

# i. Convert list to tuple
subject_list = ["Java", "C++", "Cloud"]
converted_tuple = tuple(subject_list)

print("\nConverted Tuple:", converted_tuple)

# j. Sort tuple of numbers in ascending order
numbers = (45, 12, 89, 21, 7)

sorted_numbers = tuple(sorted(numbers))

print("\nSorted Tuple:", sorted_numbers)

# k. Repeat tuple 3 times
repeat_tuple = ("DS", "ML")

print("\nRepeated Tuple:", repeat_tuple * 3)

# l. Check immutability of tuple
sample = ("Python", 301)

try:
    sample[1] = 999

except TypeError as e:
    print("\nTuple is immutable! Error:", e)
