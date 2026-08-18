# 6_10

print("S109 Neetu Salunkhe")

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

# Plot 2023 sales
plt.plot(months, sales_2023, color="blue", linestyle="--",
         marker="o", label="2023")

# Plot 2024 sales
plt.plot(months, sales_2024, color="green", linestyle="-",
         marker="s", label="2024")

# Find highest sales of 2024
max_sales = max(sales_2024)
max_index = sales_2024.index(max_sales)

# Add annotation
plt.annotate("Highest Sales: 400",
             xy=(months[max_index], max_sales),
             xytext=("Apr", 360),
             arrowprops=dict(arrowstyle="->"))

# Add title and labels
plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")

# Add legend
plt.legend()

# Save the plot
plt.savefig("sales_comparison.png")

# Display the plot
plt.show()
