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
for n1 in range(999,0,-1):
    for n2 in range(999,0,-1):
        if is_palyndrome(str(n1*n2)):
            res = str(n1*n2)
            stop = True
            break
    if stop:
        break
print(res)
