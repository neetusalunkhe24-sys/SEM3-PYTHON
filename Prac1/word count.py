#1e. Count words

sentence = input("Enter a sentence: ")

words = len(sentence.split())
characters = len(sentence)

print("Number of words:", words)
print("Number of characters:", characters)
print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())
print("With underscores:", sentence.replace(" ", "_"))
