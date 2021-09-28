#!/usr/bin/env python3

"""
Project Euler, problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

# I'll just brute force it

num = 2 ** 1000
num_to_str = str(num)
tot = 0
for i in num_to_str:
    tot += int(i)
print(tot)
