s = "ind!avi*ce"
output = ""

for ch in s:
    if ch.isalnum():
        output += ch

print(output)
