#!/usr/bin/env python3

"""
Project Euler, problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
res = 0

while(number!=res):
  res = number
  for num in range(2,number):
      if number%num == 0:
          number = number//num 
          break
print(number)
