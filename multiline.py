import re

text = """first line
second line
third line"""

pattern = r"^second"

match = re.search(pattern, text, re.M)  # re.M = ^ and $ match each line

if match:
    print("Found:", match.group())
else:
    print("Not found.")
