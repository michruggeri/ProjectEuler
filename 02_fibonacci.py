#!/usr/bin/env python3

"""
Project Euler, problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""    

limit = 4e6
num_1 = 0
num_2 = 1
total = 0

while True:
    num_1,num_2 = num_2,num_1+num_2
    if num_2 > limit:
        break
    if num_2%2 ==0:
        total += num_2
print(total)
