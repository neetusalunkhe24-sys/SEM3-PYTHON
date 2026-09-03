#9c.

print("S109 Neetu Salunkhe")

import pandas as pd

# Read the employee salary dataset
df = pd.read_csv("employee_salary.csv")

# 1. Display Name and Salary
print("Name and Salary:")
print(df[["Name", "Salary"]])

# 2. Employees with salary greater than 50000
print("\nEmployees earning more than 50000:")
print(df[df["Salary"] > 50000])

# 3. Employees with experience greater than 5 years
print("\nEmployees with experience above 5 years:")
print(df[df["Experience"] > 5])

# 4. Female employees
print("\nFemale Employees:")
print(df[df["Gender"] == "Female"])

# 5. IT Department employees
print("\nIT Department Employees:")
print(df[df["Department"] == "IT"])

# 6. Employees with salary > 50000 and experience > 5 years
print("\nEmployees satisfying both conditions (Salary > 50000 AND Experience > 5):")
print(df[(df["Salary"] > 50000) & (df["Experience"] > 5)])
