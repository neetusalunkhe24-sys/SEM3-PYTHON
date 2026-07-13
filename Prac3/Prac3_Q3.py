#Prac3_Q3

print("Name: Neetu")
print("Roll no.: S109\n")

from datetime import datetime

# Get the current date and time
current_date = datetime.now()

print("Current Date in Different Formats:\n")

# a. YYYY-MM-DD
print("a. YYYY-MM-DD      :", current_date.strftime("%Y-%m-%d"))

# b. DD-MM-YYYY
print("b. DD-MM-YYYY      :", current_date.strftime("%d-%m-%Y"))

# c. Month Day, Year
print("c. Month Day, Year :", current_date.strftime("%B %d, %Y"))

# d. Weekday, Month Day, Year
print("d. Weekday, Month Day, Year :", current_date.strftime("%A, %B %d, %Y"))
