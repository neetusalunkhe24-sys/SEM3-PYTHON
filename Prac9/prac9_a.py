#9a.

print("S109 Neetu Salunkhe")

import pandas as pd

# Create dataset
data = {
    "Student_ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Name": ["Anaya", "Vivek", "Isha", "Arjun", "Meera", "Aditya", "Riya", "Nikhil"],
    "Age": [20, 19, 21, 20, 19, 21, 20, 19],
    "Gender": ["Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male"],
    "Course": ["BSc IT", "BSc CS", "BSc CS", "BSc IT",
               "BSc CS", "BSc IT", "BSc CS", "BSc IT"],
    "Marks": [82, 76, 91, 68, 87, 73, 95, 79]
}

df = pd.DataFrame(data)

# 1. Display complete dataset
print("Complete Dataset:")
print(df)

# 2. Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# 3. Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# 4. Display number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

# 5. Display column names
print("\nColumn Names:")
print(df.columns)

# 6. Display basic information
print("\nDataset Information:")
df.info()

# 7. Display statistical information
print("\nStatistical Information:")
print(df.describe())
