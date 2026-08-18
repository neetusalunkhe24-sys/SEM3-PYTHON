# 6_9

print("S109 Neetu Salunkhe")

import matplotlib.pyplot as plt
import numpy as np

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

categories = ["A", "B", "C", "D"]
values = [20, 35, 25, 40]

scatter_x = [5, 7, 8, 7, 6, 9, 5]
scatter_y = [99, 86, 87, 88, 100, 86, 103]

data = np.random.normal(0, 1, 100)

# Create 2x2 grid
plt.figure(figsize=(10, 8))

# Top-left: Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Top-right: Bar Chart
plt.subplot(2, 2, 2)
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Bottom-left: Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(scatter_x, scatter_y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Bottom-right: Histogram
plt.subplot(2, 2, 4)
plt.hist(data, bins=20)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
