print("Name: Neetu")
print("Roll no.: S109\n")

from datetime import datetime

#Step 1: Ask the user to enter a timestamp
timestamp = float(input("Enter a timestamp (e.g., 1690915200): "))

#Step 2: Convert timestamp to datetime object
date = datetime.fromtimestamp(timestamp)

#Step 3: Print the date in readable format
print("Converted date:", date.strftime("%Y-%m-%d %H:%M:%S"))
