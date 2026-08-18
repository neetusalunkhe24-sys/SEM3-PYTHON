# 6_7

print("S109 Neetu Salunkhe")

import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random numbers using normal distribution
data = np.random.normal(0, 1, 100)

# Plot histogram with 20 bins
plt.hist(data, bins=20)

# Add grid
plt.grid(True)

plt.title("Histogram of Normal Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
