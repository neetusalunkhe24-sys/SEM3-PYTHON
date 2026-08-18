# 6_8

print("S109 Neetu Salunkhe")

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

plt.figure(figsize=(10, 4))

# First plot
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Second plot
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Square Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()
plt.show()
