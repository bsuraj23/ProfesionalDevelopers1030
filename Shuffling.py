import random

def manual_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):          # go from last index to 1
        j = random.randint(0, i)          # pick a random index from 0 to i
        arr[i], arr[j] = arr[j], arr[i]   # swap the values
    return arr



import random

a = [10, 20, 30, 40]

for i in range(len(a)):
    j = random.randint(0, len(a) - 1)
    a[i], a[j] = a[j], a[i]

print(a)

