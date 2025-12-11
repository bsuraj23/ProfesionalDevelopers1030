'''
The prime factors of 13195 are 5, 7, 13 and 29. 
What is the largest prime factor of the number 600851475143? 
'''
n = 600851475143
fac = 2 #start with smallest factor =>2

while fac*fac<=n: #2*2=4 <= n? yes     
    if n%fac==0: # n%2==0? no
        n//=fac # integer division
    else:
        fac+=1  #increment if n is not even

print("Largest prime factor:", n)


'''
Explanation:
Keep dividing the number by its smallest possible factor until only the largest prime factor remains.

1. Start with the smallest factor: 2
2. If 2 divides the number:
        We divide the number and keep dividing again and again.
3. If 2 does NOT divide the number:
        We increase the factor to 3, then 4, then 5… (incrementing)
4. Every time we find a factor, we divide the number to make it smaller.
5. When no smaller factors are left, the remaining number is the largest prime factor.

# EX: let n=84 and fac =2
 
while fac*fac - 2*2<=84? yes 
    if 84%2==0? yes
        84//2= 42 i.e. n=42

while 2*2<=42? yes
    if 42%2==0? yes
        42//2= 24 n=21

while 2*2<=21? yes
    if 21%2==0? no

    else: fac+=1
        fac = 3

while 3*3<=21? yes
    if 21%3==0? yes
        21//3=7 n=7

while 3*3<=7? no 
    stop the loop

now n=7 is the largest prime factor of 84.
(When no smaller factors are left, 
 the remaining number is the largest prime factor.)

'''