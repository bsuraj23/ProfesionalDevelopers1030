n = 600851475143   # number to factor
i = 2              # start checking from smallest prime

while i * i <= n:  # loop until i reaches sqrt(n)
    if n % i == 0:  # if i divides n
        n = n // i  # divide n by i
    else:
        i += 1      # otherwise check next number

print(n)            # remaining n is the largest prime factor


