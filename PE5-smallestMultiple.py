'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
(Ans: 232792560)
'''

import math
from functools import reduce

# Compute LCM of numbers from 1 to 20
result = reduce(math.lcm, range(1, 21))  # math.lcm computes the least common multiple of two numbers.
                                         # reduce applies it across the whole range 1–20.
print(result)
#--------------------------------------------------------------
''' 
using lcm formula i.e. "lcm(a, b) = (a * b) / gcd(a, b)"
'''
a = 1
for i in range(1, 21):
    a = a * i // math.gcd(a, i)

print(a)
