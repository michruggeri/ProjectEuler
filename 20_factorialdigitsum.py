#!/usr/bin/env python3

"""
Project Euler, problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def fact(x):
    if x < 2:
        return 1
    return x * fact(x-1)

N= 100
factorial = str(fact(N))
tot = 0
for digit in factorial:
    tot += int(digit)
print(tot)
