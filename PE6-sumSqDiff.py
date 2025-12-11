'''
The sum of the squares of the first ten natural numbers is,
            1^2+2^2+...+10^2=385.

The square of the sum of the first ten natural numbers is,
            (1+2+...+10)^2=55^2=3025.

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 
                3025 −385 =2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
'''

# sum of squares of n natuarl nos. formula => sn= n*(n+1)*(2n+1)/6
# square of the sum of n natural nos. => sq = (n*(n+1)/2)^2 i.e (1+2+...+n)^2
# difference b/w sn & sq => d=sn-sq

sn=0
n=100
sn=n*(n+1)*((2*n)+1)/6
print("Sum of squares of 100 natural numbers:", sn)
sq= (n*(n+1)/2)**2
print("Square of the sum:",sq)
d=sq-sn
print("Difference b/w sum of squares and sqauare of the sum:",d)
