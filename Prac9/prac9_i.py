#9i.

print("S109 Neetu Salunkhe")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

# 1. Bar Chart - Product vs Sales
plt.figure(figsize=(10, 6))
plt.bar(df["Product"], df["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Line Chart - Order ID vs Sales
plt.figure(figsize=(10, 6))
plt.plot(df["Order_ID"], df["Sales"], marker="o", linestyle='-', color='red')
plt.xlabel("Order ID")
plt.ylabel("Sales Amount")
plt.title("Sales Trend by Order")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram - Sales Distribution
plt.figure(figsize=(10, 6))
plt.hist(df["Sales"], bins=5, edgecolor='black', color='skyblue')
plt.xlabel("Sales Amount")
plt.ylabel("Number of Orders")
plt.title("Distribution of Sales Amount")
plt.tight_layout()
plt.show()

# 4. Pie Chart - Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%", 
        colors=['gold', 'lightgreen'], startangle=90, explode=(0.05, 0))
plt.title("Sales Distribution by Category")
plt.tight_layout()
plt.show()
