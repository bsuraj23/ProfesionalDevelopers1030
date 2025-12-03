# what is recursion 
# recursion = A function calling itself again and again 
# until a stopping point is reached

def countdown(n):
    if n == 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

countdown(100)

# Factorial using recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) # 120