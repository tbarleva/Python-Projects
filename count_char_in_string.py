# Write a program that counts all characters in a string except for space (" ")
# Print all the occurrences in the following format: "{char} -> {occurrences}"

text = input()
occurrences = {}

for char in text:
    if char != " ":
        occurrences[char] = occurrences.get(char, 0) + 1
for char, count in occurrences.items():
    print(f"{char} -> {count}")
