#Prac3_Q2

from bs4 import BeautifulSoup

print("=== HTML Word Search Program ===")
print("Name: Neetu")
print("Roll no.: S109\n")

# Step 1: Open and read the HTML file
with open("example.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Step 2: Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Extract visible text
text = soup.get_text()

# Step 4: Ask the user for a word
search_word = input("Enter the word to search: ")

# Step 5: Search the word
if search_word.lower() in text.lower():
    print(f"\nThe word '{search_word}' was found.")
else:
    print(f"\nThe word '{search_word}' was NOT found.")

print("\nExtracted Text:")
print(text)

print("\nProgram Created By: Neetu")
