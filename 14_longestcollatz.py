#!/usr/bin/env python3

"""
Project Euler, problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all
starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# This is done by brute force. A smarter method could take advantage of 
# memorizing chain lenghts (more memory intensive, but it should not be a
# problem...).

def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

counts = []
nmax = 1000000 
for i in range(1,nmax):
    count = 1
    num = i
    while num != 1:
        count += 1
        num = collatz(num)
    counts.append(count)

mlen = max(counts)
print(range(1,nmax)[counts.index(mlen)],mlen)
