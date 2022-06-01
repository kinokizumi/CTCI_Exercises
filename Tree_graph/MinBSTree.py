#!/usr/bin/python3

#########################
#
# This script makes a BST with min length out of a sorted (increasing) array
#
#########################

from collections import deque

#########################

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

## Solution 1: root = midpt of arr, pass L/R subarr recursively => O(N) time

def MinBSTree(array):
    if len(array) < 1:
        return None

    mid_idx = len(array) // 2
    left_arr = array[:mid_idx]
    right_arr = array[mid_idx+1:]
    
    root = Node(array[mid_idx])
    root.left = MinBSTree(left_arr)
    root.right = MinBSTree(right_arr)
    return root

#########################

def printTree(root):
    visited = deque([root])
    while len(visited) > 0:
        curr = visited.popleft()
        print(curr.val)
        child = []
        if curr.left:
            visited.append(curr.left)
            child.append(curr.left.val)
        if curr.right:
            visited.append(curr.right)
            child.append(curr.right.val)
        print(child)

#########################
            
array = [ i  for i in range(1, 10) ]
root = MinBSTree(array)
printTree(root)
