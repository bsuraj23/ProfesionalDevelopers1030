import re

pattern = re.compile(r"""
    (\d{3})   # area code
    -         # dash
    (\d{3})   # first 3 digits
    -         # dash
    (\d{4})   # last 4 digits
""", re.X)    # re.X allows comments and multi-line format

phone = "123-456-7890"

match = pattern.search(phone)

if match:
    print("Phone number parts:", match.groups())
else:
    print("Invalid phone number.")
