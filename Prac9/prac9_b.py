#9b.

print("S109 Neetu Salunkhe")

import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# 1. Display dataset
print("Student Dataset:")
print(df)

# 2. Display first 10 records
print("\nFirst 10 Records:")
print(df.head(10))

# 3. Find number of students
print("\nNumber of Students:")
print(len(df))

# 4. Display column names
print("\nColumn Names:")
print(df.columns)

# 5. Find average marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# 6. Find average attendance
print("\nAverage Attendance:")
print(df["Attendance"].mean())
