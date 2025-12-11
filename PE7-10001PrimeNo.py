'''
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''
# create a list of prime nos. using list comprehension
# access the 100001th prime no using index

prime=[]
for num in range(2,10000000):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):   
        prime.append(num)
    if len(prime) == 10001:   # stop early (saves time)
        break

print(prime[10000])
