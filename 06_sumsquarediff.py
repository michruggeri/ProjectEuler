#!/usr/bin/env python3

"""
Project Euler, problem 6

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... +10) ** 2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
NM = 100
nums = list(range(1,NM+1))
num2 = [n**2 for n in nums]
#for i,j in zip(nums,num2):
#    print(i,j)
diff = 0
for i in nums:
    for j in nums:
        if i!=j:
            diff += i*j
sum_sq = sum(num2)
sq_sum = (sum(nums))**2
print(f"Computing sums: {sq_sum} - {sum_sq} = {sq_sum-sum_sq}")
print(f"Using only double products: {diff}")
