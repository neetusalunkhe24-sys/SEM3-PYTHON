# 6_3

print("S109 Neetu Salunkhe")

import matplotlib.pyplot as plt

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

plt.bar(categories, scores)

plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Student Scores")

plt.show()
