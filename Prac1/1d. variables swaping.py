#1d. swap two variables

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

numbers = [10, 20, 30, 40]

swap(numbers, 0, 2)

print("Updated List:", numbers)
