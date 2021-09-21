#!/usr/bin/env python3

"""
Project Euler, problem 10 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

NM = 2000000
primes = []
total = 0
for n in range(2,NM):
    for prime in primes:
        if n%prime == 0:
            break
    else:
        primes.append(n)
        total += n

print(total)
