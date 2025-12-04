import re

text = "Start\nmiddle\nEnd"

pattern = r"Start.*End"

match = re.search(pattern, text, re.S)  # re.S = dot matches newline

if match:
    print("Matched full span:")
    print(match.group())
else:
    print("No match.")
