#!/usr/bin/env python3

"""
Project Euler, problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples = []
limit = 1000

for num in range(1,limit):
    if num%3==0 or num%5==0:
        multiples.append(num)

#for mult in multiples:
#    print(mult)

print(sum(multiples))
