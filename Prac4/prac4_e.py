#4e.

print("Name: Neetu Salunkhe")
print("Roll no.: S109")

import numpy as np

arr = np.array([15, 43, 24, 65, 74, 59])

max_value = np.max(arr)

filter_arr = arr[arr == max_value]

print("Original Array:", arr)
print("Maximum Value:", max_value)
print("Filtered Array:", filter_arr)
