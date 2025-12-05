fruit = "mango"
ch = "g"
found = False

for letter in fruit:
    if letter == ch:
        found = True
        break

if found:
    print("Present")
else:
    print("Not Present")
