#!/usr/bin/python3

#############################
#
# This script makes 3 stacks from a single array
#
#############################

## Solution 1: Fixed size stacks  

def Error(msg):
    print(msg)
    exit()

class FixedMultiStack:
    
    def __init__(self, nbStacks, stackSize):
        self.nbStacks = nbStacks
        self.capacity = stackSize
        self.values = [0] * nbStacks * stackSize
        self.sizes = [0] * nbStacks

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.capacity

    def GetTopIndex(self, stackNum):
        offset = stackNum * self.capacity
        size = self.sizes[stackNum]
        return offset + size - 1

    def push(self, stackNum, item):
        if self.isFull(stackNum):
            Error(f"Stack {stackNum} is full")
        self.sizes[stackNum] += 1
        self.values[self.GetTopIndex(stackNum)] = item

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            Error(f"Stack {stackNum} is empty")
        topIndex = self.GetTopIndex(stackNum)
        item = self.values[topIndex]
        self.values[topIndex] = 0
        self.sizes[stackNum] -= 1

#############################

array = [2,3,5,6,8,9,11]
nbStacks = 3
stackSize = len(array)//nbStacks + (len(array)%nbStacks > 0)

Stacks = FixedMultiStack(nbStacks, stackSize)
counter = 0
for stackNum in range(0, nbStacks):
    limit = min(len(array), (stackNum+1) * stackSize)
    while counter < limit:
        Stacks.push(stackNum, array[counter])
        counter += 1

print(Stacks.values, Stacks.sizes)

