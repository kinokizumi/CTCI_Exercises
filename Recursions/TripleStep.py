#!/usr/bin/python3

######################
#
# This script counts the nb of ways to reach n steps by increments of 1, 2, 3
#
######################

import numpy as np

######################

## Solution 1: Top-down non dynamic => O(3^N) time

#def TripleStep(n):
#    if n == 0:
#        return 1
#    if n == 1:
#        return TripleStep(n-1)
#    if n == 2:
#        return TripleStep(n-1) + TripleStep(n-2)
#    if n >= 3:
#        return TripleStep(n-1) + TripleStep(n-2) + TripleStep(n-3)

## Solution 2: Top-down, dynamic

#def TripleStep(n):
#    memo = np.zeros(n + 1, int)
#    return Helper(n, memo)
#
#def Helper(n, memo):
#    if n < 0:
#        return 0
#    if n == 0:
#        return 1
#    for i in range(1, n+1):
#        if memo[i] == 0:
#            memo[i] = Helper(i-1, memo) + Helper(i-2, memo) + Helper(i-3, memo)
#    return memo[n]

def TripleStep(n):
    a = 1
    b = 1
    c = a + b
    for i in range(3, n+1):
        s = a + b + c
        a = b
        b = c
        c = s
    return s

######################

n = 5
answer = 13
print( TripleStep(n) == answer )
