#!/usr/bin/env python3

"""
Project Euler, problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def get_div_sum(num):
    div_sum = 0
    for i in range(1,num//2+1):
        if num % i == 0:
            div_sum += i
    return div_sum

def find_friend(num):
    candidate = get_div_sum(num)
    if num == get_div_sum(candidate) and num!=candidate:
        return candidate
    return -1

total = 0
nmax = 10000 
for a in range(nmax):
    friend = find_friend(a)
    if friend > 0:
        total += a

print(total)
