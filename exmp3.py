import re
text="ramakrishna"
vowels="aeiou"
result=""
for char in text:
    if char not in vowels:
        result+=char
print(result)

    