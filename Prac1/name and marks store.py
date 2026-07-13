#1e. Name and Marks storage

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Details")
for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)
print("Class Average =", average)

top_student = max(students, key=students.get)

print("Highest Marks Student =", top_student)
print("Marks =", students[top_student])
