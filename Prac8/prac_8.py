#8.

print("S109 Neetu Salunkhe")

#step 1 - Import libraries

import seaborn as sns
import matplotlib.pyplot as plt

#step 2 - Load dataset
tips = sns.load_dataset("tips") #small dataset included in Seaborn
print(tips.head()) #show first 5 rows

#step 3 - Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

#step 4 - Show the plot
plt.title("Restaurant Bill vs Tip")
plt.show()
 
