#Prac3_Q1

print("Name: Neetu")
print("Roll no.: S109\n")

# Step 1: Open and read the file
with open("sample.txt", "r") as file:
    text = file.read()

# Step 2: Ask the user for the word to search
search_word = input("Enter the word to search: ")

# Step 3: Search for the word
if search_word.lower() in text.lower():
    print(f"The word '{search_word}' was found in the file.")
else:
    print(f"The word '{search_word}' was NOT found in the file.")

