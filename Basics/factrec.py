def fact(input):
    if input == 0:
        return 1
    return input * fact(input-1)
print(fact(5))