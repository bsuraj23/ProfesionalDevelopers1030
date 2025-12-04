

def fib(n):
    a, b = 1, 2
    sum = 0
    
    while a < n:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b

    return sum
print("Even sum of Fibonacci is :",fib(4000000))


