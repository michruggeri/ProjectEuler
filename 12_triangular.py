#!/usr/bin/env python3

"""
Project Euler, problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

    1 : 1
    3 : 1,3
    6 : 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

# To speed up things I use the fact that each triangular number is equal to the
# partial sum of the series of natural numbers, get the divisors of n and n+1/2
# and multiply the numbers of divisors to get the total

ndiv = 500
n = 0
nm = 0
while True:
    n+=1
    if n%2 == 0:
        n2 = n//2
        n1 = n+1
    else:
        n1 = n
        n2 = (n+1)//2
        
    d1 = 0
    d2 = 0
    for p in range(1,n1+1):
        if n1 % p == 0:
            d1 += 1
    for p in range(1,n2+1):
        if n2 % p == 0:
            d2 += 1
    if d1*d2 > ndiv:
        num = n*(n+1)//2
        break
print(num)
