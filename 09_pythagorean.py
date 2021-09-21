#!/usr/bin/env python3

"""
Project Euler, problem 9 

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
found = False
for c in range(1,1000):
    for b in range(1,c):
        for a in range(1,b):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a,b,c,a*b*c)
                found = True
                break
        if found:
            break
    if found:
        break
