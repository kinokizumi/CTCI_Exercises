#!/usr/bin/python3

###################
#
# This script checks if two strings are in permutation
#
###################

## Solution 1: Hash table => O(N) time, O(N) space

#def IsPermutation(str1, str2):
#    record = {}
#    if len(str1) != len(str2):
#        return False
#
#    for char in str1:
#        if char in record:
#            record[char] += 1
#        else:
#            record[char] = 1
#
#    for char in str2:
#        if char in record:
#            record[char] -= 1
#            if record[char] < 0:
#                return False
#        else:
#            return False
#
#    return True

## Solution 2: Sum char val => O(N) time, O(1) space

def IsPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    sum1 = 0
    sum2 = 0
    for char in str1:
        sum1 += ord(char)
    for char in str2:
        sum2 += ord(char)
    return sum1 == sum2

###################

str1 = "abogfea, QHIkotlmz"
str2 = "og fea,mQHabIkotlz"
answer = True

print(IsPermutation(str1, str2) == answer)
