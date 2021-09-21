#!/usr/bin/env python3

"""
Project Euler, problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def get_factors(num,facs):
    while num > 1:
        for n in range(2,num+1):
            if num%n == 0:
                if n in facs.keys():
                    facs[n] += 1
                else:
                    facs[n] = 1
                num = num//n
                break

factors = dict()
number = 20

lnum = list(range(number+1))
factorlist = []
for num in lnum:
    factors = dict()
    get_factors(num,factors)
    factorlist.append(factors)

totfactors = dict()
for num in lnum:
    for key in factorlist[num].keys():
        if key not in totfactors.keys() or totfactors[key] < factorlist[num][key]:
            totfactors[key] = factorlist[num][key]

prod = 1
for key,value in totfactors.items():
    print(f"{key}: {value}")
    prod *= key ** value
print(prod)
