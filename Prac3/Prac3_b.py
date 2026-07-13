print("Name: Neetu")
print("Roll no.: S109\n")

from bs4 import BeautifulSoup

# Step 1: Open and read the HTML file
with open("Python.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Extract and print all the text from the HTML
text = soup.get_text()

print("Extracted Data:")
print(text)
