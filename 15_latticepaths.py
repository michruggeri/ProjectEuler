#!/usr/bin/env python3

"""
Project Euler, problem 15 

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# Each path must have exactly 20 moves to the right and 20 moves downwards. Each path
# has the same probability, so I get the inverse probability of the path
# ddddddddddddddddddddrrrrrrrrrrrrrrrrrrrr, 
# i.e. 20/40 * 19/39 * ... * 1/11 * 1
# to get the overall number of paths.

n_grid = 20
prod = 1
for i in range(n_grid,0,-1):
    prod = prod / (i/(i+n_grid))
print(prod)
