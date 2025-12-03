sum = 0
print("Multiples of 3 0r 5")
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
