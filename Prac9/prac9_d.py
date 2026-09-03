#9d.

print("S109 Neetu Salunkhe")

import pandas as pd

df = pd.read_csv("employee_salary.csv")

# 1. Sort employees according to salary in ascending order
print("EMPLOYEES SORTED BY SALARY (LOWEST TO HIGHEST):")
print("=" * 60)
print(df.sort_values("Salary").to_string(index=False))

# 2. Sort employees according to salary in descending order
print("\nEMPLOYEES SORTED BY SALARY (HIGHEST TO LOWEST):")
print("=" * 60)
print(df.sort_values("Salary", ascending=False).to_string(index=False))

# 3. Sort employees according to experience in descending order
print("\nEMPLOYEES SORTED BY EXPERIENCE (MOST TO LEAST):")
print("=" * 60)
print(df.sort_values("Experience", ascending=False).to_string(index=False))

# 4. Display the top 5 highest paid employees
print("\nTOP 5 HIGHEST PAID EMPLOYEES:")
print("=" * 60)
print(df.sort_values("Salary", ascending=False).head(5).to_string(index=False))

# 5. Display the bottom 3 lowest paid employees
print("\nBOTTOM 3 LOWEST PAID EMPLOYEES:")
print("=" * 60)
print(df.sort_values("Salary").head(3).to_string(index=False))
