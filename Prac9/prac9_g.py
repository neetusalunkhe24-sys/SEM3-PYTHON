#9g.

print("S109 Neetu Salunkhe")

import pandas as pd

df = pd.read_csv("student_performance.csv")

# Calculate overall average marks across all subjects
df["Average_Marks"] = df[["English", "Mathematics", "Computer"]].mean(axis=1)

print("Average Marks:", df["Average_Marks"].mean())
print("Maximum Marks:", df["Average_Marks"].max())
print("Minimum Marks:", df["Average_Marks"].min())
print("Median Marks:", df["Average_Marks"].median())
print("Standard Deviation:", df["Average_Marks"].std())
print("Average Attendance:", df["Attendance"].mean())
print("Number of Students:", df["Name"].count())
print("Students scoring above 75 in all subjects:", ((df["English"] > 75) & (df["Mathematics"] > 75) & (df["Computer"] > 75)).sum())
