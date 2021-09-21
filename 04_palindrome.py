#!/usr/bin/env python3

"""
Project Euler, problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palyndrome(strin):
    nirst = strin[::-1]
    return strin == nirst

stop = False
res = ""
maxpal = -1
fact1,fact2 = -1,-1
for n1 in range(1,1000):
    for n2 in range(1,1000):
        prod = n1*n2
        if is_palyndrome(str(prod)) and prod > maxpal:
            maxpal = prod
            res = str(prod)
            fact1 = min(n1,n2)
            fact2 = max(n1,n2)
print(f"{res} = {fact1} x {fact2}")
