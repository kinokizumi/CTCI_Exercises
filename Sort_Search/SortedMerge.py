#!/usr/bin/python3

######################
#
# This script merge two sorted list A, B together
#
######################

def SortedMerge(A, B, endA):
    end = len(A) - 1
    endB = len(B) - 1
    while endB >= 0:
        if endA >= 0 and A[endA] > B[endB]:
            A[end] = A[endA]
            endA -= 1
        else:
            A[end] = B[endB]
            endB -= 1
        end -= 1
    return A

######################

A = [2, 3, 5]
B = [1, 3, 4, 6]

endA = len(A) - 1
for i in range(len(B)):
    A.append(None)

print(SortedMerge(A, B, endA))
