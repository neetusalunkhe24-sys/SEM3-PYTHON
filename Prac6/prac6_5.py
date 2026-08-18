# 6_5

print("S109 Neetu Salunkhe")

import matplotlib.pyplot as plt

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

explode = [0, 0, 0, 0.1]

plt.pie(scores, labels=categories, autopct="%1.1f%%", explode=explode)

plt.title("Student Scores")
plt.show()
