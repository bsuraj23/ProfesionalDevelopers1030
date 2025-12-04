import re

text = "Hello World"
pattern = r"hi"

match = re.search(pattern, text, re.I)  # re.I = ignore case

if match:
    print("Match found!")
else:
    print("No match.")
