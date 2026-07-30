#5d.

import pandas as pd

# Create a Series
age = pd.Series([18, 20, 22, 19, 21, 23])

print("Original Series:")
print(age)

# Filter using Boolean array
filtered_age = age[age >= 20]

print("\nFiltered Series:")
print(filtered_age)
