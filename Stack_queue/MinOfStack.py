#!/usr/bin/python3

#########################
#
# This script tracks and returns the min elem of a stack
#
#########################

## Solution 1: Each node tracks the current min => O(N) space

class Node:
    def __init__(self, data, minval):
        self.val = data
        self.min = minval

class Stack:
    def __init__(self):
        self.values = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.values[self.size-1]

    def push(self, data):
        if self.isEmpty():
            item = Node(data, data)
        else:
            top = self.peek()
            item = Node(data, min(data, top.min))
        self.values.append(item)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            item = self.values[self.size-1]
            self.values[self.size-1] = None
            self.size -= 1
        return item

    def min(self):
        if self.isEmpty():
            return None
        else:
            return self.peek().min

## Solution 2. use auxiliary stack to track min => O(1)
## need to define a child class for the aux stack
## advanced level

#########################

stk1 = Stack()
stk1.push(4)
stk1.push(2)
stk1.push(9)
print(stk1.min())
stk1.push(3)
stk1.push(7)
stk1.push(1)
print(stk1.min())
stk1.pop()
print(stk1.min())
