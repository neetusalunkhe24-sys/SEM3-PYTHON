#9h.

print("S109 Neetu Salunkhe")

import pandas as pd

df = pd.read_csv("student_performance.csv")

# Number of students in each course
print("Number of Students in Each Course:")
print(df.groupby("Course")["Name"].count())

# Average marks for each course (overall average across all subjects)
print("\nAverage Marks by Course:")
print(df.groupby("Course")[["English", "Mathematics", "Computer"]].mean())

# Maximum marks for each course
print("\nMaximum Marks by Course:")
print(df.groupby("Course")[["English", "Mathematics", "Computer"]].max())

# Average attendance for each course
print("\nAverage Attendance by Course:")
print(df.groupby("Course")["Attendance"].mean())
