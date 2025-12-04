fruit = "mango"
thing = "bat"

found_g = False
for ch in fruit:
    if ch == 'g':
        found_g = True
        break
print(found_g)

found_b = False
for ch in thing:
    if ch == 'b':
        found_b = True
        break
print(found_b)

for ch in fruit:
    if ch == 'f':
        print("f is present in fruit")
        break

for ch in thing:
    if ch == 'a':
        print("a is present in thing")
        break

  