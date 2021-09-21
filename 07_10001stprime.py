#!/usr/bin/env python3

"""
Project Euler, problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

howmany = 10001
n=1
primes = []
while True:
    n+=1
    for prime in primes:
        if n%prime == 0:
            break
    else:
        primes.append(n)
    if len(primes) == howmany:
        break
print(primes[-1])
