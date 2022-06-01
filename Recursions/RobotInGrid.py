#!/usr/bin/python3

##########################
#
# This script finds a path for a robot that moves right and down 
# to get from top left to bottom right while certains cells are banned
#
##########################

import numpy as np

##########################

## Sol.1: Simple recursion => worst O(2^(r+c)) time, tighter bound O((r+c)!/r!c!)

#def RobotInGrid(r, c, grid, path):
#    if r < 0 or c < 0 or grid[r, c] == 0:
#        return False
#    isorigin = (r==0 and c==0)
#    if isorigin or RobotInGrid(r-1, c, grid, path) or RobotInGrid(r, c-1, grid, path):
#        position = (r, c)
#        path.append(position)
#        return True
#    return False

## Sol.2: Dynamic recursion => O(rc) time

def RobotInGrid(r, c, grid, path, cache):
    position = (r, c)
    if position in cache:
        return False
    if r < 0 or c < 0 or grid[r, c] == 0:
        cache.append(position)
        return False
    isorigin = (r==0 and c==0)
    if isorigin or RobotInGrid(r-1, c, grid, path, cache) \
    or RobotInGrid(r, c-1, grid, path, cache):
        path.append(position)
        return True
    cache.append(position)
    return False


##########################

def forbidenCell(r, c, grid):
    grid[r, c] = 0

r = 4
c = 5
grid = np.ones((r, c), int)
forbidenCell(1, 0, grid)
forbidenCell(2, 3, grid)
forbidenCell(1, 4, grid)
forbidenCell(0, 3, grid)

path = []
cache = []

print(grid)
print(RobotInGrid(r-1, c-1, grid, path, cache), path)
print(cache)
